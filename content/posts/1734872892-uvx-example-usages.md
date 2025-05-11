+++ 
date = 2024-12-22T13:08:12Z
title = "List of very handy uvx use-cases"
description = ""
slug = "" 
tags = ["python", "development"]
categories = ["development"]
externalLink = ""
series = []
+++

### Open Marimo 

```shell
uvx marimo edit --sandbox
```

Also

```shell
uvx marimo tutorial intro
```

![images/2024/12/22/1734873549-1.png](/images/2024/12/22/1734873549-1.png)

### iPython with packages

```shell
uvx --with pandas,yfinance ipython
```

![images/2024/12/22/1734873549-2.png](/images/2024/12/22/1734873549-2.png)

### Convert files to markdown

```shell
uvx markitdown ssrn-4990063.pdf
```

### Aider.chat

```shell
uvx aider
```

### Clean up .pyc files and __pycache__ directories

```shell
uvx pyclean .
```

Collected from this [Reddit thread](https://www.reddit.com/r/Python/comments/1guf2fh/if_you_use_uv_what_are_your_use_cases_for_uvx/)

### Run Open WebUI

```shell
uvx open-webui@latest serve
```

### Run Autogen Studio

```shell
uvx autogenstudio@latest ui --port 8081
```

### Run llm (CLI) with Ollama

```shell
uvx --with llm-ollama llm -m llama3.1:latest "Fun facts about Squid Game"
```

Other examples in official [docs](https://github.com/simonw/llm/blob/main/docs/setup.md)

```shell
uvx --with llm-claude-3 llm -m claude-3.5-haiku 'fun facts about skunks'
```

## Run MLX VLM Models

```shell
uv run --with mlx-vlm \
  python -m mlx_vlm.generate \
  --model Qwen/Qwen2-VL-2B-Instruct \
  --max-tokens 1000 \
  --temp 0.0 \
  --image ~/Documents/Screenshots/2024/11/01/20241101_082217.png \
  --prompt "Describe image in detail, include all text"
```

```shell
uv run --with mlx-vlm --with torch \
  python -m mlx_vlm.generate \
  --model mlx-community/SmolVLM-Instruct-bf16 \
  --max-tokens 1000 \
  --temp 0.0 \
  --image https://image.png \
  --prompt "Describe image in detail, include all text"
```

```shell
uv run --with f5-tts-mlx \
  python -m f5_tts_mlx.generate \
  --output gen.wav \
  --text "On December 7, 1941, an unprepared United States was attacked at Pearl Harbor, crippling much of the US fleet. Less than four years later, US deployed a new and unimaginably destructive weapon—a weapon that, just a few years before, had been considered science fiction."
```

```shell
uvx --from mlx-audio mlx_audio.tts.generate \
    --model mlx-community/Dia-1.6B-6bit \
    --text "[S1] Dia can now run on your Mac thanks to MLX. [S2] You get full control over scripts and voices. [S1] Wow. Amazing. (laughs)"
```
