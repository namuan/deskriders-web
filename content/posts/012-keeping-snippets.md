+++ 
date = 2020-01-27T10:13:04Z
title = "A Simple setup to remember one-liners/code snippets"
description = ""
slug = "" 
tags = ["productivity", "shell", "tools"]
categories = ["productivity"]
externalLink = ""
series = []
+++

Here is a simple setup explaining a comment I made on [Reddit](https://www.reddit.com/r/datascience/comments/euad2v/how_do_you_make_sure_a_tool_you_learned_in_the/ffo9bvt).

All I have is a notes.txt under my home directory where the snippets (one-liners) are stored in the following format. 
Note that I don't store block of code or longer text here as they'll become difficult to search. 

```
find . -type f -name '*.txt' -exec sed -i '' s/this/that/g {} + # search and replace sed find
```

It starts with the command then # and a brief comment on what it does.

The notes.txt file is just a soft link to a file stored in a Dropbox shared folder so that it can be synced across devices.

Here are a couple of bash helpers to work with the notes file.

1. **fnote**

fnote=find note

A simple function defined in a bash profile to search within the notes file. 

```
function fnote() { grep "$@" ~/notes.txt }
```

Then I can do the following to filter out any lines.

```
$ fnote epoch
*  date +%s # epoch time
```

2. **en**

en=edit notes

A bash alias to open up notes.txt file in your favourite editor.

```
alias en='code ~/notes.txt'
```

Then just typing `en` will open up the notes.txt file for me to edit.

So, that's it. Pretty simple but very effective.

Let me know what you think and share if you have anything similar in your daily workflow.

