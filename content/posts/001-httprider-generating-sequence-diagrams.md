+++ 
date = 2019-10-13T07:45:14Z
title = "Generating sequence diagrams with HttpRider"
description = ""
slug = "" 
tags = ["plantuml", "python", "api"]
categories = ["httprider"]
externalLink = ""
series = []
+++

Most tools consider an HTTP API call as a single request but that is not usually the case. An API call is surrounded by a sequence of other APIs which makes it easy to understand the context of the use case. 

In HttpRider, I've recently introduced an exporter for sequence diagrams. So a collection of HTTP calls can be easily exported to sequence diagrams using PlantUML/MermaidJS.

> [HttpRider](https://github.com/namuan/http-rider "HttpRider") is an open source cross platform desktop client for working with JSON APIs 

Here is an example:

![](/images/001/httprider-multiple-calls.png)

To help the tool understand the different participants, the title of each call needs to follow this convention, for eg.  
[Client -> Gateway] Make payment

Where Client and Gateway are two different actors in a sequence diagram. In this case, HttpRider will try to extract the actors/participants between [source -\> target] and renders it in plantuml syntax.

![](/images/001/httprider_plantuml_exporter.png)

The full diagram can be rederend using [the online tool](https://www.planttext.com). Here is the [link](https://www.plantuml.com/plantuml/img/jLFlIyCm4FsUl-B8nx3OpatjnYp38LFmHtKJ11aIcjiijar9KwN8_dUJTQWRGnIqXVPwoRthlVSoB8tGfifIGaTfWhcXFAHZOV1LrBGFZ4NNaobZG9-CAVgUrzu_slFjtUu7lkzxXIeD9JfN1a4dYoS33GfvQDx0GrYZpU1IF2CKeixS1iBO6Gg9kcICZ5HkR99Fwm87S_i1iKgLFgOQ9GtPm7Ev43nlK1gTv8lGyyWz7ocjCHKcKJa_bp-jO-ocGbr39BJ8NFEgH9sBxCUDBIUYJfMGjlQDWBseAxTiqTkgB35DuSG-QAjP4vcgBArzQFQkSYyYhLn1sszz9kFAZfF7ZdOwFedeQcL9bWHp2OvXyY6CrUZE_ZLCKByaCQw46fz-ezC2jsHQ8v67TU24-WevWmkbdgjYbTmKwvvV_OgjBRet-DizMzHuP6Eyt_fmru1Rk3CRsFRHBaV-vP1hapYVFIRIoHjqU_DUnp_a1pA8UNVUxlBUF0XuHtQwXnW8iT-H_-2VeOtiKOTt "HttpRider PlantUML") to the generated diagram from the above calls. 

![](/images/001/httprider_plantuml_rendered.png)

A quick video demonstration

{{< youtube 4Asr_4iOxUM >}}