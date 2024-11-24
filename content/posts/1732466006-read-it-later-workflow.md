+++ 
date = 2024-11-24T16:33:26Z
title = "Streamlining reading and managing bookmarked links"
description = "A quick overview of my workflow to collect, organize, and publish reading links using iOS Shortcuts, Reminders, and a Python script in Pythonista."
slug = "" 
tags = ["readitlater", "reminders"]
categories = ["workflow", "productivity"]
externalLink = ""
series = []
+++

Here is a brief recap of the workflow I use to collect links to read later.

It starts with a "Shortcut," which is available on all iOS/Mac devices.

It is either something I want to read today:

![images/2024/11/24/1732467148-1.png](/images/2024/11/24/1732467148-1.png)

Or push it back to tomorrow:

![images/2024/11/24/1732467148-2.png](/images/2024/11/24/1732467148-2.png)

The links end up in a separate "Reminders" list, which makes it easy to manage.

![images/2024/11/24/1732467148-3.png](/images/2024/11/24/1732467148-3.png)

Using Reminders as a way to organize reading links is quite useful, as it nags you at regular intervals. 
And if I'm not keen to read something, I simply schedule it back by a month or two. 

Every weekend, I also run a script to collect all the links I bookmarked over the last week.
The exported list is then published on this blog.

It looks like this:

https://www.deskriders.dev/posts/1732465541-linklist-2024-11-24/

The script is [here](https://github.com/namuan/py-ios-scripts/blob/main/reminder-markdown.py), which runs in Pythonista.
