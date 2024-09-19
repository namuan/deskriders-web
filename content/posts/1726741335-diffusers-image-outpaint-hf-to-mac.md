+++ 
date = 2024-09-19T11:22:15+01:00
title = "Running Diffusers Image Outpaint Huggingface demo locally on a Mac"
description = "Clone HuggingFace and use different Pytorch backend"
slug = "" 
tags = ["diffusers", "huggingface"]
categories = ["demos"]
externalLink = ""
series = []
+++

See demo [here](https://x.com/namuan_twt/status/1836711982340214788)

Clone HuggingFace space locally

```shell
git clone https://huggingface.co/spaces/fffiloni/diffusers-image-outpaint
```

Create Virtual Environment and Install Dependencies

```shell
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Update source to use `mps` backend

![images/2024/09/19/1726741576.png](/images/2024/09/19/1726741576.png)

Run gradio application. It'll take a little time to download all models required to run this space.
If stuck then exit the process and try again. It should print a link to localhost to open the application.

```shell
venv/bin/gradio app.py
```

