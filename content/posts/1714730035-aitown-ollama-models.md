+++
date = 2024-05-03T10:53:56+01:00
title = "Setup AiTown with Pinokio and run with your own models"
description = "Set up AiTown, a virtual town platform, using Pinokio, a framework for building and managing custom AI models, to deploy and experiment with your own AI creations in a safe, scalable, and collaborative environment."
slug = "" 
tags = ["llm", "ollama"]
categories = []
externalLink = ""
series = []
+++

* Download [pinokio](https://pinokio.computer) and Setup AiTown

```shell
cd $HOME/pinokio/api/aitown.git/app
eval "$(conda shell.bash hook)" && conda deactivate && conda deactivate && conda deactivate && conda activate $HOME/pinokio/api/aitown.git/app/node18
```

* Shell 1:
```shell
./convex-local-backend
```

* Shell 2:
```shell
npm run dev
```

* Switch model

First backup Llama3

```shell
ollama cp llama3:latest llama3-backup:latest
```

Switch model

```shell
ollama rm llama3:latest; ollama cp openhermes:latest llama3:latest
```

Restore llama3 from backup
```shell
ollama rm llama3:latest; ollama cp llama3-backup:latest llama3:latest
```

Verify
```shell
ollama list
```
