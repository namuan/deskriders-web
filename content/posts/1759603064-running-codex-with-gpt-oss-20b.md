+++ 
date = 2025-10-04T19:37:45+01:00
title = "Running OpenAI Codex with locally running GPT OSS 20b model"
description = ""
slug = "" 
tags = ["llm", "codex"]
categories = ["programming"]
externalLink = ""
series = []
+++

## Llama.cpp

Install llama.cpp

```shell
brew install llama.cpp
```

Run `llama-server`

```shell
llama-server -hf ggml-org/gpt-oss-20b-GGUF  --ctx-size 0 --jinja -ub 2048 -b 2048 --port 1234
```

The above command is suggested for devices less than 96GB RAM. See reference for other commands.

## Codex

```shell
brew install codex
```

## Setup config.toml file

```shell
take ~/.codex
vim ~/.codex/config.toml
```

```toml
[model_providers.lms]
name = "LM Studio"
base_url = "http://localhost:1234/v1"
[profiles.gpt-oss-20b-lms]
model_provider = "lms"
model = "gpt-oss:20b"
```

Run codex

```shell
codex --profile gpt-oss-20b-lms
```

## Reference:

https://github.com/ggml-org/llama.cpp/discussions/15396
