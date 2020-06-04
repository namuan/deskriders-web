+++ 
draft = false
date = 2020-06-04T22:11:58
title = "Handy Bash/Zsh function to generate PlantUML diagrams"
description = "Creating a simple Bash/Zsh function wrapping PlantUML so that we can use it from anywhere"
tags = ["plantuml", "bash"]
categories = ["tooltips"]
externalLink = ""
series = []
+++

In this short clip, we'll look at creating a simple Bash/Zsh function wrapping PlantUML so that we can use it from anywhere.

#### Requirements:

* PlantUML: [Direct Download](http://sourceforge.net/projects/plantuml/files/plantuml.jar/download)

Download it where you can easily refer to it. 

```bash
nmn$ ls -l $TOOLS_HOME/plantuml/plantuml.jar
-rw-r--r--@ 1 nmn  staff  7985304  9 Nov  2019 /Users/nmn/tools/plantuml/plantuml.jar
```

Next, we'll create a function and put that in bash/zsh profile so that it can be loaded automatically on each session.

```bash
function plantuml() {
    NAME=$1
    cat $NAME | java -DPLANTUML_LIMIT_SIZE=8192 -jar $TOOLS_HOME/plantuml/plantuml.jar -pipe > $NAME.png
    open $NAME.png
}
```

Then you can call this function with the file name.

```bash
plantuml sample.png
```

Once you have it setup, this will convert the provided plantuml file to a PNG image and open it up using the default PNG viewer.

Here it is in action

{{< youtube Wy02jNNkhIE >}}

📝:

👉 Tested on MacOS but should work on earlier versions and all flavours of Linux

