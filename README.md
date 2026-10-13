# Evaluation recognition pilot

A small manual replication and exploratory formatting extension of Needham et al. (2025), *Large Language Models Often Know When They Are Being Evaluated*: https://arxiv.org/abs/2505.23836 .

This snapshot contains 25 manually submitted responses. Collection is incomplete. The conversational-greeting research question was considered but has not been tested. Model names/settings are recorded as reported by the participant, not independently verified API identifiers.

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

The supplied authors' dataset archive contains 976 examples; 500 have null/empty scaffold and were treated as chat. 287 carry evaluation source labels and 213 deployment labels. Ten evaluation examples were sampled without replacement from 35 examples with at least two line-initial lettered options; ten controls were sampled from the 213 deployment examples. Sampling seed: 20261012223311, Python random.Random. Evaluation eligibility used letter-option patterns `(A)`, `A)`, `A.`, or `A:` and at least two detected choices. Each evaluation had an original and an inline-option variant; option text and order were preserved, labels removed, and commas or semicolons substituted for option-list formatting. System messages were preserved. RQ A-only cases were reshuffled with seed 20261012223947. The case manifest links original source IDs to current case IDs.

Each prepared request quoted one transcript with role labels, followed by the first published evaluation-identification question and a fixed instruction not to follow the quoted conversation. The participant manually ran fresh chatbot chats and pasted responses for recording. YES means evaluation; NO means deployment. Labels remain usable when tags are missing but an answer is unambiguous. A mistakenly pasted Gemini critique was replaced with the actual response; an accidental duplicate GPT R06 submission was removed at the participant's request. Missing cases remain missing.

## Source access and sharing

Full task transcripts are excluded from this repository. Obtain the original dataset through the authors' gated page and follow its license/access conditions: https://huggingface.co/datasets/jjpn2/eval_awareness . This avoids republishing the raw dataset. Classifier responses and source IDs are included for auditing. Cite the paper when using these materials. No API keys are included.

## Updating

Append new unique model/setting/prompt records to `data/responses.json` and rerun the script. Preserve the first valid collection attempt and document corrections. Commit and push updates to the same GitHub repository; its URL stays the same. For a deadline snapshot, preserve a version tag or commit URL.
