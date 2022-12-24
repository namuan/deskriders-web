+++
date = 2022-12-24T16:57:13Z
title = "Installing PyAudio on M1 Mac"
description = "Instructions to setup PyAudio pip module on M1 Mac"
slug = "" 
tags = ["pyaudio", "audio"]
categories = ["setup"]
externalLink = ""
series = []
+++

If you are getting the following error when installing `pyaudio`

```shell
  × Building wheel for pyaudio (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [16 lines of output]
      running bdist_wheel
      running build
      running build_py
      creating build
      creating build/lib.macosx-13-arm64-cpython-310
      copying src/pyaudio.py -> build/lib.macosx-13-arm64-cpython-310
      running build_ext
      building '_portaudio' extension
      creating build/temp.macosx-13-arm64-cpython-310
      creating build/temp.macosx-13-arm64-cpython-310/src
      clang -Wno-unused-result -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -isysroot /Library/Developer/CommandLineTools/SDKs/MacOSX13.sdk -DMACOSX=1 -I/usr/local/include -I/usr/include -I/Users/nnn/workspace/voice-koder/venv/include -I/opt/homebrew/opt/python@3.10/Frameworks/Python.framework/Versions/3.10/include/python3.10 -c src/_portaudiomodule.c -o build/temp.macosx-13-arm64-cpython-310/src/_portaudiomodule.o
      src/_portaudiomodule.c:31:10: fatal error: 'portaudio.h' file not found
      #include "portaudio.h"
               ^~~~~~~~~~~~~
      1 error generated.
      error: command '/usr/bin/clang' failed with exit code 1
```

Make sure you uninstall any existing `pyaudio` module before running the commands.

```shell
brew uninstall portaudio
pip uninstall pyaudio
```

Then run the following commands

```shell
python3 -m pip install --upgrade pip setuptools wheel
brew install portaudio --HEAD
export CFLAGS="-I/opt/homebrew/include"
export LDFLAGS="-L/opt/homebrew/lib"
python3 -m pip install pyaudio
```
