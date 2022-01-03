+++
date = 2022-01-03T10:38:32
title = "Generate Homebrew dependencies graph"
description = ""
slug = ""
tags = []
externalLink = ""
series = []
+++
        

Tap dependent package
```shell
brew tap martido/homebrew-graph
```

**Generate dot file**
```shell
brew graph -f dot --installed --highlight-leaves -o graph.dot
```

**Clean dot file and generate gif**
```shell
cat graph.dot | sfdp -x -Goverlap=scale -Nshape=circle -Gspinles=curved -Tgif > deps.gif
```

The output will be in `deps.gif`

![](/images/2022/01/03/542973917575786.png)