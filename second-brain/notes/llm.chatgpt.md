---
id: 66vzyuualtdivw2cm4xqosv
title: ChatGPT
desc: ""
updated: 1707251588073
created: 1706083927396
---

- [State of GPT](https://www.youtube.com/watch?v=bZQun8Y4L2A)
- [OpenAI Documentation](https://platform.openai.com/docs/overview)
- [Cookbook](https://cookbook.openai.com/)
- [Get up and running with the OpenAI API](https://platform.openai.com/docs/quickstart?context=python)

## [Andrew Ng: Opportunities in AI - 2023](https://www.youtube.com/watch?v=5p248yoa3oE)

```python
# Install the OpenAI Python library
pip install openai

#import openai packages
from openai import OpenAI
import os

# Authentication with API key
OPENAI_API_KEY = "ChallengeACPR"
openai.api_key = os.getenv("OPENAI_API_KEY")

# First step: defining a function
def get_response_to_prompt(prompt):
    response = openai.ChatCompletion.create(
    model = "gpt-4",
    message = [{"role": "user", "content":prompt}],
    temperature = 0.7
    )
    return response.choices[O].message["content"]

# Second step: prompting
prompt = """
Classify the text below, delimited by three dashes (-), as having either a positive or negative sentiment.

---
<text>
---
"""

# Last, but not least: printing the LLM completion
response = get_response_to_prompt
print(response)
```
