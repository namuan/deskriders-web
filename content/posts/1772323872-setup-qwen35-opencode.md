+++ 
date = 2026-03-01T00:11:13Z
title = "Quick Setup: Qwen3.5-27B Local with llama.cpp + OpenCode"
description = "Step-by-step guide to running Qwen3.5-27B locally using llama.cpp and integrating it with OpenCode for local AI development."
slug = "quick-setup-qwen35-llama-opencode"
tags = ["AI", "LLM", "Qwen3.5", "llama.cpp", "OpenCode", "Local AI", "AI Development"]
categories = ["AI", "Development", "Tools"]
externalLink = ""
series = []
+++

**1. Install llama.cpp**  
```bash
brew upgrade llama.cpp
```

**2. Run model (downloads Q6_K on first run)**  
```bash
llama-server -hf unsloth/Qwen3.5-27B-GGUF:Q6_K --port 9090
```

More [options](https://huggingface.co/unsloth/Qwen3.5-27B-GGUF?local-app=llama.cpp) & quants: https://unsloth.ai/docs/models/qwen3.5#qwen3.5-27b

**3. Add to OpenCode config (~/.opencode/config.json)**  
```json
{
  "provider": {
    "llama.cpp": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "llama.cpp local",
      "options": {
        "baseURL": "http://127.0.0.1:9090/v1"
      },
      "models": {
        "qwen35-27b-local": {
          "name": "Qwen3.5-27B (Local)",
          "limit": {
            "context": 262144,
            "output": 32000
          }
        }
      }
    }
  }
  // merge with existing config
}
```

**Done.**  
Q6_K ≈ 23 GB RAM/VRAM, near-lossless quality, 256K context.  
Lower quants (Q5_K_M, Q4_K_M) if faster/slimmer needed.
