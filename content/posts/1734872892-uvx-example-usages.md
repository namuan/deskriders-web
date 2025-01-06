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
