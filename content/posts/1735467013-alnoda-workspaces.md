+++ 
date = 2024-12-29T10:10:13Z
title = "Setting Up Alnoda: A Dockerized Development Workspace"
description = "A step-by-step guide to configuring and customizing Alnoda Desktop, an open-source containerized development environment with VS Code integration and port management"
slug = "" 
tags = ["docker", "environments", "vscode"]
categories = ["development"]
externalLink = ""
series = []
+++

**Alnoda desktop** provides a dockerized development environment.

According to the [GitHub repo](https://github.com/bluxmit/alnoda-workspaces)

> Open-source portable containerized workspaces. Isolate your work, make backups, copy, move between computers and cloud seamlessly.

You can start it up with the following command

```shell
docker run --name space-1 -d -p 8020-8040:8020-8040 --restart=always alnoda/alnoda-workspace
```

Although due to port conflicts, I had to change to different port sequence `(18020-18040)`.

```shell
docker run --name space-1 -d -p 18020-18040:8020-8040 --restart=always alnoda/alnoda-workspace
```

Once it is up, go to <http://localhost:18020> see the environment

![images/2024/12/29/1735467607-1.png](/images/2024/12/29/1735467607-1.png)

You can install other applications using Terminal.
Note that the Terminal will start at the pre-configured port which didn't work as I had to change the port mapping.
It is a little inconvenient to update the ports manually. I'm sure there is a setting somewhere to configure it.

```text
http://localhost:8021 -> http://localhost:18021
```

Then I can install Open VSCode

```shell
wrk install openvscode
```

**Restart the workspace after installation to activate the changes**

```shell
wrk kill
```

After the workspace is restart, go to the Home Screen again to see the new application

![images/2024/12/29/1735467607-2.png](/images/2024/12/29/1735467607-2.png)

Again, we need to manually update the port number

http://localhost:18030/?folder=%2Fhome

And you do get a fully featured dockerized IDE

![images/2024/12/29/1735467607-3.png](/images/2024/12/29/1735467607-3.png)