+++ 
date = 2020-06-05T07:47:18
title = "Tooltip 15: Bash/Zsh function to export SVG diagrams using PlantUML"
description = "Looking at creating a simple Bash/Zsh function for export SVG diagrams using PlantUML"
tags = ["plantuml", "bash"]
categories = ["tooltips"]
externalLink = ""
series = []
+++

In this short clip, we'll look at creating a simple Bash/Zsh function for export SVG diagrams using PlantUML.

#### Requirements:

* PlantUML: [Direct Download](http://sourceforge.net/projects/plantuml/files/plantuml.jar/download)

Place it where you can easily refer to it. 

```bash
nmn$ ls -l $TOOLS_HOME/plantuml/plantuml.jar
-rw-r--r--@ 1 nmn  staff  7985304  9 Nov  2019 /Users/nmn/tools/plantuml/plantuml.jar
```

Next, we'll create a function and put that in bash/zsh profile so that it can be loaded automatically on each session.

```bash
function plantsvg() {
    NAME="$1"
    cat ${NAME} | java -DPLANTUML_LIMIT_SIZE=8192 -jar $TOOLS_HOME/plantuml/plantuml.jar -tsvg -pipe > ${NAME}.svg
    open -a Firefox.app ${NAME}.svg
}
```

Once you have it setup, this will export the provided plantuml file to an SVG image and open it up using Firefox.
You can change the application used to open this SVG by replacing `Firefox.app` with the another application.

Here it is in action

{{< youtube ytSB-cjAKzA >}}

📝:

👉 Tested on MacOS but should work on earlier versions and all flavours of Linux

