+++ 
date = 2025-01-18T10:42:41Z
title = "EPUB to Conversational Audio: AI-Powered Podcast Generator"
description = "Convert EPUB files into engaging audio podcasts using AI. This script leverages MLX Qwen models for transcript generation and Kokoro Onnx TTS for natural voice synthesis, delivering captivating audio outputs effortlessly."
slug = "" 
tags = ["TTS", "Podcast", "MLX", "Books"]
categories = ["Audio Processing", "eBook Conversion", "Text-to-Speech"]
externalLink = ""
series = []
+++

This script extracts text from an EPUB file, formats it, and converts it into an engaging audio podcast.
It uses AI-based transcript generation, rewriting, and text-to-speech synthesis to create a conversational and captivating audio output.

Here is the [source code](https://github.com/namuan/llm-playground/blob/main/epub-to-audio.py)

```shell
git clone https://github.com/namuan/llm-playground.git
```

## Pre-Requisites:

* MLX Qwen2.5 Models:
  * These will be downloaded when the script runs for the first time.

```text
FIRST_PASS_LLM = "mlx-community/Qwen2.5-14B-Instruct-4bit"
SECOND_PASS_LLM = "mlx-community/Qwen2.5-7B-Instruct-4bit"
```

Although you can configure a different MLX model if you already have it downloaded.

It uses multiple passes to generate a final transcript based on the architecture described [here](https://github.com/meta-llama/llama-cookbook/tree/main/end-to-end-use-cases/NotebookLlama)

* Kokoro Onnx Models:
  * You will also need to download Kokoro Onnx TTS and voices from https://github.com/thewh1teagle/kokoro-onnx
  * Or you can run the following wget commands.

  ```shell
  wget https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files/voices.json
  wget https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files/kokoro-v0_19.onnx
  ```

Please keep note of the downloaded directory and update the `# CONFIG` section of the script with the correct paths. 
See `KOKORO_MODEL_VOICES_PATH` and `KOKORO_MODEL_PATH`.

You can also try changing the Speakers by using one of the voices listed here: https://github.com/thewh1teagle/kokoro-onnx?tab=readme-ov-file#voices

Here is the complete config section from the script.

```python
### Config

OUTPUT_DIR = Path.cwd() / "target" / "epub_pods"
OUTPUT_DIR.mkdir(exist_ok=True)

KOKORO_MODEL_VOICES_PATH = Path.home() / "models/onnx/kokoro/voices.json"
KOKORO_MODEL_PATH = Path.home() / "models/onnx/kokoro/kokoro-v0_19.onnx"
kokoro = None  # Lazy init

KOKORO_SPEAKER_1 = "bm_george"
KOKORO_SPEAKER_2 = "af_sarah"

SECOND_PASS_FILE_NAME = "second_pass.pkl"
INITIAL_PASS_FILE_NAME = "initial_pass.pkl"
FORMATTED_CHAPTER_FILE_NAME = "formatted_chapter.txt"

FIRST_PASS_LLM = "mlx-community/Qwen2.5-14B-Instruct-4bit"
SECOND_PASS_LLM = "mlx-community/Qwen2.5-7B-Instruct-4bit"

### CONFIG (END)
```

Once everything is set up, you can run the script by providing the path to the ePub file.
Although I do recommend starting with just generated the formatted text to see if everything looks good.


```shell
./epub-to-audio.py --text-only path/to/book.epub
```

Then next step, you can generate a subset of chapters to check the voices and output
This will only process the first 2 chapters of the book. 
Keep an eye on the output it currently skips chapters with < 3 lines.

```shell
./epub-to-audio.py _path/to/book.epub -v --chapters 2
```

All output is generated under `target/epub_pods/<book-name>` folder.
