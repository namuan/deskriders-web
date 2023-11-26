+++
date = 2023-11-26T11:01:49Z
title = "Weekly Notes 2023-11-26"
description = ""
slug = "" 
tags = []
categories = []
externalLink = ""
series = []
+++

#### [AI narrator](https://github.com/Pwntus/replicate-narrator)
This is like the [original](https://github.com/cbh123/narrator) demo but using downloadable models. 
It requires using replicate API but it'll be cool to run everything locally.

#### [SVD-WebUI](https://github.com/hylarucoder/svd-webui)
Looks like an interface to Stable Video diffusion but I can't get it to work on a Mac.

#### How to create a custom GPT from an SQLite3 database

Name: API Tool Finder
Instructions: 
```text
The API Tool Finder GPT is tailored to assist users in identifying the most suitable API tools for their needs. 
It interacts with an SQLite database that contains the api_resources table with the following structure

(0, 'id', 'INTEGER', 1, None, 1),
 (1, 'name', 'TEXT', 0, None, 0),
 (2, 'short_description', 'TEXT', 0, None, 0),
 (3, 'website', 'TEXT', 0, None, 0),
 (4, 'category', 'TEXT', 0, None, 0),
 (5, 'tags', 'TEXT', 0, None, 0),
 (6, 'screen_shot', 'TEXT', 0, None, 0),
 (7, 'long_description', 'TEXT', 0, None, 0),
 (8, 'is_opensource', 'BOOLEAN', 0, None, 0)]

Instructions: 
Use SQL Like query on the following four columns to find a matching answer

Column 1:  name
Column 2: short_description
Column 3: category
Column 4: tags

If a match is found then display all the information about the tools in a markdown formatted table view. Ignore the screen_shot and long description column when displaying the answer.
Always make sure that the answer can be referenced back to a row or rows in the database table. 
If a match is not found then just saw that a match is not found
```

Knowledge: Attach database file

#### [rags](https://github.com/run-llama/rags)
Create Chat with your data using natural language

#### [Introducing Tuna - A Tool for Rapidly Generating Synthetic Fine-Tuning Datasets](https://blog.langchain.dev/introducing-tuna-a-tool-for-rapidly-generating-synthetic-fine-tuning-datasets/)
Tuna is a no-code tool for quickly generating LLM fine-tuning datasets from scratch. This enables anyone to create high-quality training data for fine-tuning large language models like the LLaMas.

#### [GPT-4 Vision Alternatives](https://blog.roboflow.com/gpt-4-vision-alternatives/)
Roboflow team lists down 4 alternatives to GPT-4V namely LLaVA, BakLLaVA, Qwen-VL, and CogVLM

#### [pdm](https://github.com/pdm-project/pdm)
PDM, as described, is a modern Python package and dependency manager supporting the latest PEP standards.
The most significant benefit is it installs and manages packages in a similar way to npm that doesn't need to create a virtualenv at all!

#### [NeumAI](https://github.com/NeumTry/NeumAI)
Neum AI is a best-in-class framework to manage the creation and synchronization of vector embeddings at large scale.

#### Helper script to quickly deploy llama.cpp server

```text
bash -c "$(curl -s https://ggml.ai/server-llm.sh)"
```

* Runs on Linux and MacOS
* Can run any GGUF model from HuggingFace: https://huggingface.co/models?sort=trending&search=gguf
* Supports multiple client streams
* Support for OAI-like API using a proxy: https://github.com/ggerganov/llama.cpp/tree/master/examples/server#api-like-oai
* Recommend to deploy on a clean machine / VM

#### [LangSmith Prompt Hub](https://smith.langchain.com/hub)

#### [multi-agent-postgres-data-analytics](https://github.com/disler/multi-agent-postgres-data-analytics/tree/v6-control-flow-and-structured-response)
This is a multi-agent system that allows you to ask questions about your postgres database in natural language.
The codebase is powered by GPT-4, Assistance API, AutoGen, Postgres, and Guidance.
It's the first of many multi-agent applications that utilize LLMs (large language models) to enable reasoning and decision making with reduced need for explicit rules or logic.

#### [qa_expert](https://github.com/khaimt/qa_expert)
QA Expert is a Language Model (LLM) specifically fine-tuned for the task of Question Answering, with a strong emphasis on addressing Multi-hop Question Answering scenarios.

#### [RepoCoder](https://github.com/microsoft/CodeT/tree/main/RepoCoder)
Simple, generic, and effective framework to tackle the repository-level code completion task, which is to continue writing the unfinished code based on a broader context of the repository.

#### [LlamaIndex guide](https://nanonets.com/blog/llamaindex/)
A Complete LlamaIndex Guide

#### [LLM-Fine-Tuning](https://github.com/meetrais/LLM-Fine-Tuning)

#### [InsightSolver](https://github.com/R3gm/InsightSolver-Colab)
Colab notebooks for exploring and solving operational issues using deep learning, machine learning, and related models.




