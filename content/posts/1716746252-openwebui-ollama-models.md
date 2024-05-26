+++ 
date = 2024-05-26T18:57:32+01:00
title = "Setup OpenWebUI with Pinokio and run with your own models"
description = "Set up OpenWebUI using Pinokio."
slug = ""
tags = ["llm", "ollama"]
categories = []
externalLink = ""
series = []
+++

* Download [pinokio](https://pinokio.computer) and Setup Open WebUI

Run with a single command

```shell
cd $HOME/pinokio/api/open-webui.git && eval "$(conda shell.bash hook)" && conda deactivate && conda deactivate && conda deactivate && conda activate base && source $HOME/pinokio/api/open-webui.git/app/backend/env/bin/activate $HOME/pinokio/api/open-webui.git/app/backend/env && bash app/backend/s.sh
```
