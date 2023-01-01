+++ 
date = 2023-01-01T20:47:29Z
title = "Installing Tortoise TTS"
description = "List all the steps I took to install Tortoise TTS on my MacOS"
slug = "" 
tags = ["tts", "ai"]
categories = ["tools"]
externalLink = ""
series = []
+++

These instructions are only tested on macOS and valid on 1st of January 2023.

```shell
git clone https://github.com/neonbjb/tortoise-tts.git

cd tortoise-tts

python3.9 -m venv venv

source venv/bin/activate

pip install torch torchvision

python3.9 setup.py install

pip uninstall numpy
pip install numba

pip uninstall threadpoolctl
pip install scikit-learn==1.2.0

# Rerunning due to failures in the previous step because on mismatched versions
python3.9 setup.py install

pip install torchaudio

python tortoise/do_tts.py --text "I'm going to speak this" --voice random --preset fast

ls -l results
open results/random_0_0.wav
```


