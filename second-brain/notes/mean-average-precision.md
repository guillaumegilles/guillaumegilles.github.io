---
id: omutp4wxiv7xcir6jfvssee
title: Mean Average Precision
desc: "MAP3@"
updated: 1698872365501
created: 1698872238393
---

𝑀𝐴𝑃@3=1𝑈∑𝑢=1𝑈∑𝑘=1𝑚𝑖𝑛(𝑛,3)𝑃(𝑘)×𝑟𝑒𝑙(𝑘)

## Mean Average Precision @ 3

$𝑀𝐴𝑃@3 = 1*𝑈*∑*𝑢*=1*𝑈*∑*𝑘*=1*𝑚**𝑖**𝑛*(*𝑛*,3)*𝑃*(*𝑘*)×*𝑟**𝑒**𝑙*(*𝑘*)$ - where _𝑈_ is the number of questions in the test set, _𝑃_(_𝑘_) is the precision at cutoff _𝑘_, _𝑛_ is the number predictions per question, and _𝑟**𝑒**𝑙_(_𝑘_) is an indicator function equaling 1 if the item at rank _𝑘_ - is a relevant (correct) label, zero otherwise. - Once a correct label has been scored for an individual question in
the test set, that label is no longer considered relevant for that
question, and additional predictions of that label are skipped in the
calculation. For example, if the correct label is `A` for an observation, the following predictions all score an average precision of `1.0`.

- ## Hugging Face Trainer

  If we're using Hugging Face trainer (and training a `AutoModelForMultipleChoice`), we can add the competition `MAP@3` metric to display during training. Here is the code:

  ```python
  import numpy as np
  def map_at_3(predictions, labels):
      map_sum = 0
      pred = np.argsort(-1*np.array(predictions),axis=1)[:,:3]
      for x,y in zip(pred,labels):
          z = [1/i if y==j else 0 for i,j in zip([1,2,3],x)]
          map_sum += np.sum(z)
      return map_sum / len(predictions)

  # Define your custom evaluation function
  def compute_metrics(p):
      predictions = p.predictions.tolist()
      labels = p.label_ids.tolist()
      return {"map@3": map_at_3(predictions, labels)}
  ```

- Then when you begin your training with Hugging Face trainer, add `compute_metrics = compute_metrics` as below:

  ````python
  trainer = Trainer(
      model=model,
      args=training_args,
      tokenizer=tokenizer,
      data_collator=DataCollatorForMultipleChoice(tokenizer=tokenizer),
      train_dataset=tokenized_dataset,
      eval_dataset=tokenized_dataset_valid,
      compute_metrics = compute_metrics,
  )  ```

  ````

- https://www.kaggle.com/competitions/kaggle-llm-science-exam
- https://www.kaggle.com/competitions/kaggle-llm-science-exam/discussion/435602
