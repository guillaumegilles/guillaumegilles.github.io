---
id: ncqzttr593gh87scnokt7j9
title: Prompt Engineering
desc: ""
bibliography: dendron-pkm.bib
updated: 1706474261971
created: 1706207508926
---

## Qu’est-ce que prompt engineering

> "Prompt engineering attempts to turn an LLM into an objective, predictable, transactional API like any other API a program may interface with such as payments, in-process function calls, SaaS calls, etc. Of course, a language model is not a deterministic, 100% reliable machine, so the utility and use case must be different." [@hashimotoPromptEngineeringTransactional2023]

C’est construite méthode d’ingénierie robuste et fiable pour extraire de la valeur ou une solution d’un [[llm]] afin de résoudre un problème, _"engineering method to extracting value from LLMs"_[@hashimotoPromptEngineeringVs2023]. Il ne faut pas confondre **prompt ingineering** avec une approche _"trail and error"_ ou _"blind prompting"_ dans laquelle on essaie de trouver la bonne recette au travers un cuisine artisanale et fortuite.

## Construire une méthodologie adaptée au **prompt engineering**

1. Déterminer si le **prompt engineering** est adapté au problème qu’on cherche à résoudre. L’objectif est la résolution du problème et non pas la solution mise en place;
2. Batir un jeu complet (une douzaine) de prompt/completion afin de bien comprendre les attendus en terme d’inputs et d’outputs. Il est important de réfléchir à cette étape car, bien souvent, l’objectif est d’intégrer la slution dans un ensemble de briques technologiques;
3. Déterminer, dans un premier temps, de façon manuelle, des prompts que nous pensons être capable de générer de bon résultat pour le problème. Il existe plusieurs recommandations à ce sujet :

   - Il est préférable d’utiliser des phrases affirmatives;
   - Il est souvent préférable d’être clair et concis plutôt que d’être répétitif et long;
   - Insérer des exemples sur lesquels les LLM était susceptible de se tromper fonctionnent généralement mieux;
   - Il a été démontré que les exemples fonctionnent souvent mieux lorsqu’ils sont classés du plus court au plus long.

4. Prompt testing

With a set of candidate prompts as well as a demonstration set, we can now measure **accuracy** as a percentage of correct answers. The best way I've found to do this today is to build a simple Python script using a library like LangChain. For my testing, I usually run through each demonstration and perform the following prompt template:

```
{{prompt}}. Q: {{input}} A:
```

| Prompt     | Zero-Shot GPT3 | Zero-Shot GPT4 | Few-Shot GPT3 | Few-Shot GPT | ... |
| :--------- | :------------- | :------------- | ------------- | ------------ | :-- |
| Prompt 1   | 64             | 68             | 69            | 72           | ... |
| Prompt ... | 44             | 52             | 59            | 79           | ... |
| Prompt N   | 23             | 22             | 21            | 26           | ... |

In addition to accuracy, you also want to measure tokens used, requests used, etc. All of this will have to be taken into consideration when choosing your final prompt.

5. Choisir le prompt

Finally, you choose one of the prompt candidates to integrate into your application. This isn't necessarily the most accurate prompt. This is a cost vs. accuracy analysis based on model used, tokens required, and accuracy presented.

6. Continuous improvement

Due to the probabilistic nature of generative AI, your prompt likely has some issues. Even if your accuracy on your test set is 100%, there are probably unknown inputs that produce incorrect outputs. Therefore, you should trust but verify and add verification failures to your demonstration set in order to develop new prompts and increase accuracy.

## Les méthodes de **prompt engineering**

- zero-shot
- few-shot
- [[llm.prompt-engineering.chain-of-thoughts]]
- batched-prompt

---

- [Prompt Engineering with Llama 2](https://github.com/facebookresearch/llama-recipes/blob/main/examples/Prompt_Engineering_with_Llama_2.ipynb)
