+++
date = 2021-12-24T10:06:01
title = "Setting up Git commit template"
description = "How to setup a global Git commit template to remind you to write good commit messages."
slug = ""
tags = []
categories = ["git", "best-practices"]
externalLink = ""
series = []
+++
        
> How to setup a global Git commit template to remind you to write good commit messages.

Here is the template I like to use just to remind me about different keywords when using [conventional commit](https://www.conventionalcommits.org/en/v1.0.0/#summary)

```txt
---
fix: PATCH (Semantic versioning) .. fix! for beaking change
feat: MINOR (Semantic versioning) .. feat! for breaking change

build:, chore:, ci:, docs:, style:, refactor:, perf:, test:

BREAKING CHANGE: extends key in config file is now used for extending other config files
```

Create a file with the template.

```shell
$ cat GIT_COMMIT_TEMPLATE
---
fix: PATCH (Semantic versioning) .. fix! for beaking change
feat: MINOR (Semantic versioning) .. feat! for breaking change

build:, chore:, ci:, docs:, style:, refactor:, perf:, test:

BREAKING CHANGE: extends key in config file is now used for extending other config files
```

Configure this template globally

```shell
$ git config --global commit.template ~/workspace/GIT_COMMIT_TEMPLATE
```

It should be available next time you are committing anything. You may have to restart the application (like IntelliJ) to pick up these changes

![](/images/2021/12/496441513639431.png)


**Reference:**

https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733