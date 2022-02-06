+++
date = 2022-02-06T10:03:41
title = "Auto generate documentation for python scripts in README.md file"
description = "A simple way to keep documentation in-sync with the scripts"
slug = ""
tags = []
externalLink = ""
series = []
+++

Here is a simple way to keep README document in-sync if you have a number of things to document.

And it looks like this:

![](/images/2022/02/06/484506901615092.png)


Each script needs to response to `--help` when called which is then collected and rendered into `README.md` between a set of pre-configured tokens.

[readme_docs.py](https://github.com/namuan/bin-utils/blob/master/readme_docs.py) contains the code to generate this documentation.

It is also [configured](https://github.com/namuan/bin-utils/blob/master/.pre-commit-config.yaml#L44) as a pre-commit hook so that we always keep it up to date.

```
      - id: readme-docs
        name: Readme documentation
        description: Using [python help], inserts into README.md.
        entry: python3 readme_docs.py
        language: system
        pass_filenames: false
```

