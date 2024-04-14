---
id: m9jn8fry9clkqptfbha40n7
title: fine tuning
desc: fine tuning un LLM
updated: 1709506865552
created: 1691179382800
---

_fine tuning_ consiste a réentrâiner un [[llm]] pré-entrâiné sur un jeu de
données relatif à une problématique particulière pour améliorer les performances.
Avec le _fine tuning_ on adapte un modèle générique pour une situation spécifique.

Pour ce faire, on met à jour les **poids** du LLM pour le façonner sur mesure
aux données en question.

## [Memory-Efficient Optimizer](https://www.deeplearning.ai/the-batch/a-method-to-reduce-memory-needs-when-fine-tuning-ai-models/)

## Finetuning Techniques

1. Transfer learning

In machine learning, the practice of using a model developed for one task as the basis for another is known as transfer learning. A pre-trained model, such as GPT-3, is utilized as the starting point for the new task to be fine-tuned. Compared to starting from scratch, this allows for faster convergence and better outcomes. Using a pre-trained convolutional neural network, initially trained on a large dataset of images, as a starting point for a new task of classifying different species of flowers with a smaller labeled dataset.

2. Sequential fine-tuning

Sequential fine-tuning refers to the process of training a language model on one task and subsequently refining it through incremental adjustments. For example, a language model initially trained on a diverse range of text can be further enhanced for a specific task, such as question answering. This way, the model can improve and adapt to different domains and applications. For example training a language model on a general text corpus and then fine-tuning it on medical literature to improve performance in medical text understanding.

3. Task-specific fine-tuning

Task-specific fine-tuning adjusts a pre-trained model for a specific task, such as sentiment analysis or language translation. The model requires more data and time than transfer learning. However, it improves accuracy and performance by tailoring to the particular task. For example, a highly accurate sentiment analysis classifier can be created by fine-tuning a pre-trained model like BERT on a large sentiment analysis dataset.

4. Multi-task learning

Multi-task learning trains a single model to carry out several tasks at once. When tasks have similar characteristics, this method can be helpful and enhance the model’s overall performance. For example, training a single model to perform named entity recognition, part-of-speech tagging, and syntactic parsing simultaneously to improve overall natural language understanding.

5. Adaptive fine-tuning

In adaptive fine-tuning, the learning rate is dynamically changed while the model is being tuned to enhance performance. By doing this, you can avoid overfitting. For example adjusting the learning rate dynamically during fine-tuning to prevent overfitting and achieve better performance on a specific task, such as image classification.

6. Behavioral fine-tuning

Behavioral fine-tuning incorporates behavioral data into the process. For example, data from user interactions with a chatbot might improve a language model to enhance conversational capabilities. For instance, the fine-tuning process can enhance the model’s conversational capabilities by incorporating user interactions and conversations with a chatbot.

7. Parameter efficient fine-tuning

The size of the model is decreased during fine-tuning to increase its efficiency and use fewer resources. This technique is known as parameter efficient fine-tuning. For example, decreasing the size of a pre-trained language model like GPT-3 by removing unnecessary layers to make it smaller and more resource-friendly while maintaining its performance on text generation tasks.

8. Text-text fine-tuning

The text-text fine-tuning technique tunes a model using pairs of input and output text. This can be helpful when the input and output are both texts, like in language translation. For example, a language model can improve its accuracy in English-to-French translation tasks by fine-tuning using text-text fine-tuning with pairs of English sentences as input and their corresponding French translations as output.
