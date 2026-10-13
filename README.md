# Evaluation recognition pilot

A manual replication and exploratory formatting extension of Needham et al. (2025), *Large Language Models Often Know When They Are Being Evaluated*: https://arxiv.org/abs/2505.23836 .

This snapshot contains 25 manually submitted responses; collection is not yet complete. The conversational-greeting research question (B) was considered but not tested. Model names, settings, and responses are recorded as reported by the researcher, not independently verified API identifiers.

## Run the analysis

Python 3, no external dependencies:

```bash
python analyze.py
```

Outputs `results/summary.json`. Results are separated by model and reported reasoning setting. DeepSeek R01 used DeepThink off; R02 and R03 used it on. GPT Instant is separate from GPT Medium.

## Files

- `data/responses.json`: full classifier responses, extracted labels, source labels, conditions, settings and correction notes.
- `data/case_manifest.json`: case IDs and pairing/source metadata.
- `analyze.py`: count classifications and paired changes.
- `research_writeup.md`: preliminary findings and limitations.

## Procedure

The supplied authors' dataset archive contains 976 examples, of which 500 had chat settings (agentic were ignored for my replication experiment). 287 carry evaluation source labels and 213 deployment labels. 10 evaluation examples were sampled without replacement from 35 examples with at least two line-initial lettered options; 10 controls were sampled from the 213 deployment examples. Sampling seed: 20261012223311, Python random.Random. Evaluation eligibility used letter-option patterns `(A)`, `A)`, `A.`, or `A:` and at least two detected choices. Each evaluation had an original and an inline-option variant; option text and order were preserved, labels removed, and commas or semicolons substituted for option-list formatting. System messages were preserved. RQ A-only cases were reshuffled with seed 20261012223947. The case manifest links original source IDs to current case IDs.

Each prepared request quoted one transcript with role labels, followed by the first published evaluation-identification question and a fixed instruction not to follow the quoted conversation. I manually ran fresh chatbot chats and pasted responses for recording. 
YES means evaluation; NO means deployment. 

## Source access and sharing

Full task transcripts are excluded from this repository. Obtain the original dataset through the authors' gated page and follow its license/access conditions: https://huggingface.co/datasets/jjpn2/eval_awareness .

## Updating

Append new unique model/setting/prompt records to `data/responses.json` and rerun the script. 
