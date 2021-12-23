+++
date = 2021-12-23T18:40:25
title = "Working with asdf"
description = "Setting up asdf for managing packages"
slug = ""
tags = []
categories = []
externalLink = ""
series = []
+++
        
[asdf](https://asdf-vm.com/)

[Installation](https://asdf-vm.com/guide/getting-started.html#_1-install-dependencies)


Dependencies required (on Linux) before setting up `Python` using `asdf`

```shell
sudo apt install build-essential zlib1g-dev libbz2-dev libssl-dev libsqlite3-dev sqlite libffi-dev libbson-dev -y
```

**Adding Python plugin**

```shell
~ asdf plugin add python
```

**Installing Python**

```
~ asdf install python 3.9.1
```

**Setting up globally**

```shell
~ asdf global python 3.9.1
```

```
~ python --version
Python 3.9.1
```

**Uninstalling Python**

```shell
~ asdf uninstall python 3.9.1
```

**Adding Java plugin**

```shell
asdf plugin-add java https://github.com/halcyon/asdf-java.git
```

**List all available version**

```shell
~ asdf list-all java | grep openjdk-11.0.2
```

**Installing Java 11**

```shell
~ asdf install java adoptopenjdk-11.0.2+9
```

**Setting up JAVA_HOME**

```
~ asdf global java adoptopenjdk-11.0.2+9k

For JAVA_HOME
. ~/.asdf/plugins/java/set-java-home.zsh
```