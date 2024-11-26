+++ 
date = 2024-11-26T11:49:29Z
title = "Quick Guide to Downloading DevDocs Documentation"
description = "Set up documentation for any package to help with building LLM context"
slug = "" 
tags = ["llm", "devdocs"]
categories = ["llm", "programming"]
externalLink = ""
series = []
+++

Here is a quick way to download a copy of the documentation for any package available at `https://devdocs.io`

```shell
git clone https://github.com/freeCodeCamp/devdocs.git && cd devdocs
```

Replace the existing `Dockerfile` with this:

```Dockerfile
# Stage 1: Setup dependencies
FROM ruby:3.3.6 as builder
ENV LANG=C.UTF-8
ENV ENABLE_SERVICE_WORKER=true

WORKDIR /devdocs

RUN apt-get update && \
    apt-get -y install git nodejs libcurl4 && \
    gem install bundler && \
    rm -rf /var/lib/apt/lists/*

COPY Gemfile Gemfile.lock Rakefile /devdocs/

RUN bundle install --system && \
    rm -rf ~/.gem /root/.bundle/cache /usr/local/bundle/cache

# Stage 2: Final image
FROM ruby:3.3.6
ENV LANG=C.UTF-8
ENV ENABLE_SERVICE_WORKER=true

WORKDIR /devdocs

RUN apt-get update && \
    apt-get -y install git nodejs libcurl4 && \
    rm -rf /var/lib/apt/lists/*

# Copy installed gems and compiled assets from builder
COPY --from=builder /usr/local/bundle /usr/local/bundle
```

Now build the image.

```shell
docker build -t thibaut/devdocs .
```

Once the image is built, run this command to list all the documentation packs available:

```shell
docker run -v $(pwd):/devdocs thibaut/devdocs bash -c "thor docs:list"
```

Run the following command to download the documentation for a specific package:

```shell
docker run -v $(pwd):/devdocs thibaut/devdocs bash -c "thor docs:download css"
```

Or run this to download documentation for all available packages

```shell
docker run -v $(pwd):/devdocs thibaut/devdocs bash -c "thor docs:download --all"
```

Once downloaded, the documentation will be under `public/docs` folder

![images/2024/11/26/1732622000-1.png](/images/2024/11/26/1732622000-1.png)

The collection of html files can be cleaned up and written to a single markdown file using [trafilatura](https://trafilatura.readthedocs.io/en/latest/usage-cli.html)

```shell
uvx trafilatura --input-dir public/docs/css --markdown > css-llm.md
```
