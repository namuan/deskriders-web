+++ 
date = 2023-01-02T13:23:48Z
title = "Running Maven in Docker"
description = "Building a project in Docker using Maven"
slug = "" 
tags = ["maven", "docker"]
categories = ["productivity"]
externalLink = ""
series = []
+++

Run this from the root of a maven project

```shell
docker run -it --rm -v "$PWD":/home/src/gpt-fx -v "$HOME/.m2":/root/.m2 -w /home/src/gpt-fx maven:3.8.3-openjdk-17  mvn clean package -Ppackage
```

![image](/images/2023/01/02/1672673166.png)
