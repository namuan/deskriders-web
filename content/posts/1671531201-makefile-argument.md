+++ 
date = 2022-12-20T10:08:33Z
title = "Run a Makefile target with argument"
description = "How to run a Makefile target with arguments"
slug = "" 
tags = ["makefile"]
categories = ["tips"]
externalLink = ""
series = []
+++

Define a new `Makefile` task

```text
...
new-post: ## Create a new post with the given title (Use this with title=blah blah)
    hugo new posts/`date +%s`-$(title).md
...
```

Use it from the command line by providing a title when calling this task

```shell
make new-post title=hello-world
```

See full [Makefile](https://github.com/namuan/deskriders-web/blob/master/Makefile#L39)
