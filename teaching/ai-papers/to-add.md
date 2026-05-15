## Post-Training Optimisation: Pruning and Quantisation

Once a model is trained, it often goes through compression steps before
deployment (particularly if it needs to run efficiently on limited hardware).
Two of the most common are pruning and quantisation:

| Technique | What it does | Security consideration |
| ----------|--------------|------------------------|
| Pruning   | Removes parameters that contribute little to predictions, shrinking model size |Changes model behaviour post-training; rarely documented in detail |
| Quantisation | Reduces numerical precision of weights (e.g., 32-bit to 8-bit floats) to cut memory and compute requirements | Can degrade safety-aligned behaviour; backdoor defences tested on full-precision models may fail to detect threats in quantised versions |

## Pre-Trained Models & Fine-Tuning

A pre-trained model is one that has already been trained on a large, general-purpose dataset (the kind of web-scale corpus discussed in Task 2). These base models learn broad language understanding: grammar, facts, reasoning patterns, and world knowledge. They're produced by a small number of well-resourced organisations and then made available for others to build on, either through open weights (like Meta's LLaMA family) or through access (like OpenAI's GPT series).

Fine-tuning is the process of continuing to train one of these pre-trained models on a smaller, task-specific dataset. A healthcare company might fine-tune a base model trained on clinical documentation to improve its understanding of medical terminology. A law firm might fine-tune on case law. The result is a model with the broad capabilities of the base model, now specialised for a particular domain or use case.

What fine-tuning changes: the model's task-specific behaviour, tone, and domain knowledge.

What fine-tuning does not change: the base model weights (the billions of parameters shaped by pre-training on data the fine-tuning organisation never saw and almost certainly never audited).
The Inheritance Problem

This is where the security concern sits. When you fine-tune a pre-trained model, you inherit everything that model already contains. This includes things you cannot see and did not choose:

Biases baked in during pre-training persist.
Unexpected behaviours introduced by the base model's carry through.
Any safety alignment built into the base model is not as durable as it might appear.

This shows up in three concrete ways:

1. Safety alignment erodes, not breaks

Stanford and Princeton (https://arxiv.org/abs/2310.03693) found that the defence mechanisms of aligned LLMs can be compromised by fine-tuning on as few as 10 adversarially crafted examples (at a cost of under $0.20). Even benign fine-tuning on legitimate data degraded safety as a side effect.

Think of safety alignment like a well-worn path through a forest. The model has been trained to follow this safe path when generating responses. Fine-tuning is like adding new paths through the same forest. Even if those new paths are legitimate (like teaching medical terminology), they can gradually obscure the original safe path. The model hasn't forgotten how to be unsafe; the probability weights have just shifted, making unsafe responses more likely again. The defence mechanisms don't snap; they wear down.

2. Specialisation increases attack surface

Cisco (https://blogs.cisco.com/security/fine-tuning-llms-breaks-their-safety-and-security-alignment) found that fine-tuned models are measurably more susceptible to prompt injection than the base models they were fine-tuned on. The reason is structural: fine-tuning narrows the focus, reducing resilience to unexpected tokens. Think of it like this: a model fine-tuned on financial records gets better at financial reasoning, but also becomes more responsive to an attacker who frames their prompt in financial terms.

3. Version matters, and it's rarely tracked

Fine-tuning always targets a specific checkpoint of a base model. If that checkpoint later turned out to contain a backdoor or problematic

, every derivative inherits it, regardless of whether anyone downstream was told. Without knowing exactly which version a model was fine-tuned from, there's no way to assess that exposure after the fact.
Inheritance Tax

When your organisation deploys a fine-tuned model, you're not deploying the fine-tuning work your team did; you're deploying the entire pre-trained base beneath it. That base was shaped by a training process you didn't control, on data you didn't audit, by an organisation whose supply chain you almost certainly haven't reviewed. Fine-tuning is powerful, but it doesn't sanitise what came before it.


Model Cards

The documentation artefact designed to address this is the model card: a structured document that accompanies a model and describes what it is, how it was built, and where it falls short. The concept was introduced by Google researchers in 2019 (https://arxiv.org/abs/1810.03993) and has since become the closest thing the industry has to a standard transparency format.

A well-formed model card should give you the answers to the questions you can't get by inspecting the weights themselves:
Section 	What it should tell you
What sources were used, how they were filtered, known gaps or biases
Intended use 	What the model was designed for (and explicitly what it wasn't)
Evaluation results 	Performance metrics across different conditions and demographics
Known limitations 	Conditions under which the model is known to underperform or behave unexpectedly
Bias assessment 	Where
or evaluation may have introduced skew
Licence 	What you're legally permitted to do with the model

Think of it like a nutritional label for an

model. You can't see inside the product, but the label is supposed to tell you what went into it and what to watch out for.
The Gaps

Have you ever checked out a food label, and it all sounds good until you find out your chicken slices are only 49% chicken? Well, in practice, model cards can also be frequently incomplete, vague, or (in some cases) absent entirely. Unlike food labels, there's no regulatory requirement to produce one; as of now, it remains voluntary for most use cases. The incentive to be thorough is weak when disclosing limitations might reduce adoption. The Data Provenance Initiative (https://arxiv.org/abs/2310.16787)'s audit of over 1,800 datasets found documentation gaps throughout the
supply chain, and model cards sit at the end of that same underdocumented pipeline.

Different models use different tokenisation methods: GPT uses Byte-Pair Encoding, while BERT uses WordPiece. The same sentence produces different token sequences depending on which model you're using.

Ask an LLM the same question twice and you'll likely get different answers. This is nondeterminism: outputs vary even with identical inputs. Unlike traditional software, where the same input always produces the same output (deterministic behaviour), LLMs introduce randomness when predicting the next token. While parameters like temperature (which we'll cover below) can reduce randomness, no setting eliminates it entirely — even major providers acknowledge this.
This has massive security implications and will be at the core of any defence and mitigation discussions. As mentioned, code (for example, malware) will execute the same way every time, but a defence may work on a malicious prompt one time and fail another. This key characteristic of LLMs poses a massive challenge to the security community and industry.

---

Temperature: The Randomness Dial

Temperature is the most important parameter you'll touch. This is a numerical value, commonly ranging from 0.0 - 2.0 (which can differ between providers) that controls how "adventurous" the model is when picking its next word. For illustration's sake, consider we are examining temperature within a range of 0.0 - 2.0.

Temperature Range 	Behaviour 	Use Case
0.0 – 0.3 	Always picks the most probable token; closest to determinism 	Code generation, data extraction, factual Q&A
0.7 – 1.0 	Samples from a wider distribution; more variety and creativity 	Brainstorming, storytelling, marketing copy
1.2 – 1.5 	Coherence begins to break down; unpredictable outputs 	Experimental use only
1.5+ 	Low-probability tokens dominate; outputs can feel "drunk" 	Avoid for most tasks

---

Max Tokens: The Length Limiter

Max tokens caps how long the response can be. One token roughly equals 0.75 English words, so 100 tokens usually equals about 75 words. Set this too low and the model cuts off mid-sentence. Set it too high and you pay for rambling you don't need. Consumer models, like those on paid plans like OpenAI, charge per token, so controlling length is a cost-control measure.

Common token budgets:

    Quick answers or tight summaries: 50 - 150 tokens
    Detailed explanations: 500 - 1000 tokens
    Full articles or reports: 2000+ tokens

Just remember: max tokens doesn't guarantee the model will use them all. It's a ceiling, not a target.

---

Top-P: The Alternative Randomness Dial

Top-p (nucleus sampling) is temperature's cousin. Think of it like this: instead of turning up or down the randomness across all possible words, top-p sets a shortlist. Set top-p to 0.9, and the model only considers words that together account for 90% of the likely options. The weird, unlikely tail gets cut off entirely. The higher the value, the bigger the shortlist; the lower the value, the more restricted the model's choices.

In general, it is advised to adjust temperature OR top-p, but not both. Using both simultaneously creates unpredictable interactions because you're stacking two randomness controls. Temperature is good for most tasks; it's simpler, more intuitive, and widely understood. Top-p is better when you need the model to adapt its creativity based on context.

---

Context Window: The Memory Limit

Every model has a context window: its maximum "working memory" measured in tokens. Modern LLMs range from 8k tokens (older GPT-3.5) to 1M+ tokens (Gemini 1.5 Pro). Claude 3.5 Sonnet handles 200k tokens, enough for 150,000 words or 500 pages of text. Exceed this limit and the model silently truncates earlier context. It literally forgets the start of your conversation.

---

## prompt

Effective prompts aren't magic; they're carefully structured instructions that
guide the model toward the desired outcome. A good prompt explicitly spells out
what you want, how you want it, and any constraints to follow. Experts often
break prompts into clear components (or pillars):
  - the core instruction (task to perform)
    Instruction (task): This is the core command or action you want from the , expressed with a clear verb. For example, use commands such as "Write...", "Analyse…", "Summarise…", or "Compare..." to explicitly state the task. Being explicit with the action prevents ambiguity. It's the difference between saying "Help me with marketing" and "Draft a 300-word social media post about a new eco-friendly product aimed at millennials". Clear instructions set expectations and direct the AI's focus.
  - relevant context (background information),
    Context (background): Context provides the AI with relevant information or a scenario so it understands the situation and perspective. This can include domain details, objectives, or background documents. For instance, you might explain who the audience is, reference specific data, or even set a "system message" style role: "You are an experienced marine biologist specialising in fish". Such context steers the 's tone and content. The more relevant background you supply, the less guessing the model has to do, reducing errors. Context can also link to external sources or files (e.g., "Based on the attached report..."), ensuring the answer fits the situation.
  - the desired output format (structure/style),
    Output format (structure): Specify how you want the answer to look. This could mean asking for bullet points, a numbered list, a table, code blocks, a JSON object, or a certain word count. For example, "Summarise these 3 log samples each in a bullet point, all under 50 words". Explicitly stating format and length makes the response immediately useful. If you need a summary, specify its length; if you need code, specify language or style.
  - and any constraints (rules or limits).
    Constraints (boundaries): These are any rules or limits you impose on the response. Constraints guide the model to follow specific boundaries; for example, forbidding certain topics, enforcing a style guide, or mandating a tone. They ensure output aligns with your needs. For example, "Write an academic report on IoT devices, provide citations in MLA format, and include a bullet-pointed summary section at the end (do NOT exceed 5 bullets)". By defining constraints, you keep the AI on track and avoid unwanted directions.
	
When all these elements work together, the model has a well-defined framework for generating accurate, on-target responses. Let's break that down.

---
## Model Card Audit

### Training data

- Training data source is vague — no provenance, collection dates, or checksums provided.
- No mention of PII filtering despite scraped forum and web data in the corpus.

### Training Procedure

Fine-tuned from enterprise-base-v1.1 — a specific version with no documentation of what that version contains or whether it has known issues.

Be careful on :
- fine-tuning, what model used ?

### Evaluation

No bias evaluation, no limitations section, and a sparse evaluation section with no adversarial or red-team testing documented.

### License

Licence listed as "Custom" with no link, no terms, and no contact detail beyond the organisation name.

### Files

Model file size is significantly smaller than the base model with no documentation of what post-training modifications were applied.