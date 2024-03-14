---
id: b1yp3y13jqsz333wn1301ma
title: Hallucinations
desc: ""
updated: 1709505381210
created: 1698094847916
---

1/ what

- sentence contradictions : LLM génère des phrases contradictoires
- prompt contradictions : "write a positive revoiew of a restaurant" => "the food was bad and the service terrible"
- contradictions des faits : Barack Obama est le premier président des etats unis
- nonsensical irrevelant infor : paris capital de france paris est aussi le nom d'un chateur

  2/ why

- data quality (error noise biais)
- generation method (beam search, sampling, maximum likelihhod estimation, reinforcement learning) : introduction biais tradeoff between
  - coherence / creativity
  - accurary / novelty
    (beam search may favor high probability but generic word over low probability but specidfic words)
- input context (prompt) = missleading prompt (can cat speak english? = if we speak of garfield)

  3/ minize

- clear & specific prompt to the system
- active mitigation : setting of the llm / temperature for randomness of the input
- multishot prompting : multiple example of output to the prompt

  Dire que les LLM hallucine signifie que les LLm se comporte comme des humains.
  En réalité puisque les LLM prédise les mots les uns à la suite des autres, le modèle
  peut générer une phrase complétement cohérente, mais fausse. La réponse du LLM est une erreur statistique

  génère une phrase grammaticalement correct (forme) mais fausse (fond)

  Une stratégie de correction de ce problème est l'explainability.= knowledge graph
