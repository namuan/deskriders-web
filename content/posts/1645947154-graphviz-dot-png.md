+++ 
date = 2022-02-27T07:33:19
title = "TIL :: Graphviz 👉 PNG with docker"
description = "Converting a Graphviz dot file to png with a Docker image"
tags = ["docker", "graphviz"]
categories = ["til"]
externalLink = ""
series = []
+++

A simple Graphviz dot file. You could try generating [brew dependencies graph](https://www.deskriders.dev/posts/1640943229-brew-graph-highlight-edges/)

Create a Docker image

```docker
FROM alpine:3.5

RUN mkdir /graphviz && \
  apk add --update graphviz ttf-dejavu && \
  rm -rf /var/cache/apk/*

WORKDIR /graphviz

CMD dot -Tpng
```

Build Docker image from this file

```bash
docker build -f Dockerfile -t namuan/dot2png .
```

And then run it with the dot file

```bash
cat dependencies.dot | docker run --rm -i namuan/dot2png > dependencies.png
```
