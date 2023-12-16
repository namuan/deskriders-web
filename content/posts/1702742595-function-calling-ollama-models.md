+++ 
date = 2023-12-16T16:03:16Z
title = "Function calling using Ollama models"
description = "A simple demo to use functions with Mitral running on Ollama"
slug = "" 
tags = ["ollama", "mixtral"]
categories = []
externalLink = ""
series = []
+++

![image](/images/2023/12/16/1702744605.png)

Here is a quick breakthrough of using `functions` with [Mixtral](https://mistral.ai/news/mixtral-of-experts/) running on [Ollama](https://ollama.ai)

[Code](https://github.com/namuan/llm-playground/blob/main/local-llm-tools-simple.py) is available here.

It is built on top of [openhermes-functions](https://github.com/abacaj/openhermes-function-calling/blob/main/openhermes-functions.ipynb) by [abacaj](https://twitter.com/abacaj) 🙏

The prompt used looks like this

```text
You have access to the following tools:
{function_to_json(get_weather)}
{function_to_json(calculate_mortgage_payment)}
{function_to_json(get_directions)}
{function_to_json(get_article_details)}

You must follow these instructions:
Always select one or more of the above tools based on the user query
If a tool is found, you must respond in the JSON format matching the following schema:
{{
   "tools": {{
        "tool": "<name of the selected tool>",
        "tool_input": <parameters for the selected tool, matching the tool's JSON schema
   }}
}}
If there are multiple tools required, make sure a list of tools are returned in a JSON array.
If there is no tool that match the user request, you will respond with empty json.
Do not add any additional Notes or Explanations

User Query:
```

And ran it through the following functions

> ❓What's the weather in London, UK

> ❓Determine the monthly mortgage payment for a loan amount of $200,000, an interest rate of 4%, and a loan term of 30 years

> ❓What's the current exchange rate for GBP to EUR

> ❓I'm planning a trip to Killington, Vermont (05751) from Hoboken, NJ (07030). Can you get me weather for both locations and directions

```text
❓What's the weather in London, UK?
{
  "tools": [
    {
      "tool": "get_weather",
      "tool_input": {
        "city": "London, UK"
      }
    }
  ]
}
Total duration: 22.051592084 seconds
```

```text
❓Determine the monthly mortgage payment for a loan amount of $200,000, an interest rate of 4%, and a loan term of 30 years.
{
  "tools": [
    {
      "tool": "calculate_mortgage_payment",
      "tool_input": {
        "loan_amount": 200000,
        "interest_rate": 4.0,
        "loan_term": 30
      }
    }
  ]
}
Total duration: 25.839688083 seconds
```

The following case is where the function isn't available therefore no tools in the response.

```text
❓What's the current exchange rate for GBP to EUR?
{
  "tools": []
}
Total duration: 24.320765666 seconds
```

And the following requires multiple function calls.
Very impressed to see it returning the correct functions in the sequence

```text
❓I'm planning a trip to Killington, Vermont (05751) from Hoboken, NJ (07030). Can you get me weather for both locations and directions?
{
  "tools": [
    {
      "tool": "get_weather",
      "tool_input": {
        "city": "Killington, Vermont"
      }
    },
    {
      "tool": "get_weather",
      "tool_input": {
        "city": "Hoboken, NJ"
      }
    },
    {
      "tool": "get_directions",
      "tool_input": {
        "start": "Hoboken, NJ 07030",
        "destination": "Killington, Vermont 05751"
      }
    }
  ]
}
Total duration: 33.417602167 seconds
```
