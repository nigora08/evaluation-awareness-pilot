# Evaluation recognition under changes to answer option formatting

## Research Process

I conducted a manual classification pilot using transcripts from Needham et al. (2025). I used ChatGPT to help inspect the dataset, sample examples, prepare prompt variants, record responses, and generate analysis code. I ran the chatbot prompts and supplied their responses. A conversational-greeting extension was discussed, but the data collected in this snapshot concern option formatting and baseline classification; no greeting results are available.

Before submission, insert an accurate time log in at least 30-minute increments. Chat timestamps establish when messages were sent, not how every interval was spent; this report does not invent a time allocation.

## Team background and contributions

- Nigora
  - Background: college student with limited coding experience. Add any relevant background you want mentors to consider.
  - Contribution: [Leave blank for an individual submission, as requested by the template.]

## Research Writeup

### Question and method

Does replacing a lettered answer-option list with inline options change a current model's classification of a question as originating from an AI evaluation? This is a small conceptual replication and exploratory extension of *Large Language Models Often Know When They Are Being Evaluated* (Needham et al., 2025): https://arxiv.org/abs/2505.23836 .

From the supplied dataset, we identified 500 chat examples. We randomly sampled ten evaluation-source questions containing lettered options and ten deployment-source controls. Each evaluation question had an original and an inline-option version: option letters were removed and choices placed inline, with wording and order preserved. All other messages were retained. Controls were unchanged and were not matched on multiple-choice format.

The planned collection was 30 independent chats per model, using the first published classification question. The model was shown a quoted transcript and asked to produce YES (evaluation) or NO (deployment), with an explanation. Unlike the paper's five prompt variants and repeated trials, this pilot uses one wording and one submitted response per case. Reported model names are interface labels supplied by the participant.

### Preliminary results at the current snapshot

There are 25 responses, including 19 from GPT-6 Medium. GPT classified all 19 available cases as evaluations: 9/9 original evaluations, 4/4 inline variants, and 6/6 deployment controls. Three evaluation questions have both versions collected; all three remain YES after reformatting. Thus, no label change was observed in the three complete pairs. The remaining pairs are incomplete.

Only sparse control data exist for other models. Claude Sonnet 5.5 Medium, Gemini 3.6 Thinking, and GPT-6 Instant each classified R01 as evaluation despite its deployment source label. DeepSeek-V4.1-Flash classified R01 and R02 as evaluation and R03 as deployment. R01 had DeepThink off while R02 and R03 had it on, so these settings must not be pooled as a controlled model comparison.

R01 was checked directly against the original archive: ID `prosocial_dialog:33563`, `eval_category=false`, with identical messages. In the authors' response files, all nine tested models mostly classified this same example as evaluation: 19–25 YES responses out of 25, depending on model. This supports treating R01 as a difficult source-label case rather than assuming our sample was mislabeled during preparation.

### Interpretation and limitations

The available GPT responses show a strong tendency to choose evaluation, including on controls. That makes unchanged YES classifications after editing weak evidence: a model that chooses YES for everything would also show no change. Three complete pairs cannot establish that formatting has no effect. We cannot yet answer the conversational-greeting question or compare model families reliably.

The paper's deployment category includes sources where evaluation of the language model was not the primary purpose; it does not guarantee every example is an authentic production conversation. Errors here are disagreements with the authors' source labels. Additional limitations include the small sample, unmatched controls, public benchmark familiarity, one classification wording, manual collection, and incomplete coverage. This measures classification of quoted interactions, not spontaneous evaluation awareness, sandbagging, or deceptive intent.

### Implications

A useful next step is to finish the paired examples under fixed settings, report control false positives alongside recognition, and test a conversational greeting as a separately identified follow-up. This pilot illustrates why explanations that sound persuasive and high recognition of evaluation examples alone do not establish reliable discrimination.

Codebase: [INSERT YOUR GITHUB REPOSITORY URL HERE]
