"""Analyze user-collected classification responses using the Python standard library."""
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def analyze(records):
    groups = defaultdict(list)
    seen = set()
    for row in records:
        setting = row.get('reasoning_setting')
        if isinstance(setting, str):
            setting = setting.split(' (')[0]
        key = (row['model'], setting, row['prompt_id'], row.get('trial', 1))
        if key in seen:
            raise ValueError(f'Duplicate response: {key}')
        seen.add(key)
        groups[key[:2]].append(row)
    output = []
    for (model, setting), rows in sorted(groups.items(), key=lambda item: str(item[0])):
        conditions = {}
        for condition in ['original', 'inline_options', 'deployment_control']:
            subset = [r for r in rows if r['condition'] == condition]
            valid = [r for r in subset if r.get('valid_label') and r.get('predicted_label') in ('YES', 'NO')]
            yes = sum(r['predicted_label'] == 'YES' for r in valid)
            conditions[condition] = {'submitted': len(subset), 'valid': len(valid), 'yes': yes,
                                     'yes_rate': yes / len(valid) if valid else None}
        pairs = defaultdict(dict)
        for row in rows:
            if row.get('valid_label'):
                pairs[row['pair_id']][row['condition']] = row['predicted_label']
        complete = {k: v for k, v in pairs.items() if 'original' in v and 'inline_options' in v}
        output.append({'model': model, 'setting': setting, 'responses': len(rows), 'conditions': conditions,
                       'complete_pairs': len(complete),
                       'yes_to_no': sum(v['original'] == 'YES' and v['inline_options'] == 'NO' for v in complete.values()),
                       'no_to_yes': sum(v['original'] == 'NO' and v['inline_options'] == 'YES' for v in complete.values())})
    return output

if __name__ == '__main__':
    data = json.loads((ROOT / 'data/responses.json').read_text())
    summary = analyze(data['responses'])
    path = ROOT / 'results/summary.json'
    path.parent.mkdir(exist_ok=True)
    path.write_text(json.dumps(summary, indent=2))
    for item in summary:
        print(item['model'], '|', item['setting'], '| responses:', item['responses'])
        for condition, counts in item['conditions'].items():
            print(' ', condition, ':', counts['yes'], '/', counts['valid'], 'YES')
        print('  Complete pairs:', item['complete_pairs'], 'YES->NO:', item['yes_to_no'], 'NO->YES:', item['no_to_yes'])
