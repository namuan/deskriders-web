---
title: "Mac (Apps/Tools/Tips and Tricks)"
date: 2021-12-19T15:46:00Z
---

### Apps

* HTTP Toolkit -> https://httptoolkit.tech/
Intercept & view all your HTTP(S) Mock endpoints or entire servers Rewrite, redirect, or inject errors
Open source -> https://github.com/httptoolkit

#### Screen Drawing

Found [quickdraw](https://github.com/maxchuquimia/quickdraw) which is an app for drawing over the screen.
Unfortunately, it doesn't seem to provide any packages, and I'm unable to build it locally.
A similar application which is quite good is [Pensela](https://github.com/weiameili/Pensela).

![](/images/2021/12/pensela.png)

#### Command Line Tools

* ImageMagick Resize a bunch of images using ImageMagick

```shell
find ./static -name '*.png' | while read line; do convert -resize 1280x1280 $line $line; done
```

* Combine and convert list of images into a single PDF

```shell
convert IMG_00{09..18}.JPG IMG_0025.JPG IMG_00{19..20}.JPG IMG_0026.JPG IMG_00{21..24}.JPG Final-Doc.pdf
```

* jq: Length of array

```shell
$ echo '["123", "567", "abc"]' | jq '. | length'
```

* Shell: Pass contents of clipboard as file descriptor. It'll work with apps expecting file argument.

```shell
$ command <(pbpaste)
```

* Convert: Resize image

```shell
$ convert -quality 75% -resize 40x40 twitter.png twitter-icn.png
```
* Ctrl X-E to quickly edit current command

{{< youtube Uin5cYqY7y8 >}}

### Homebrew

__Updating packages___
```shell
brew update
```

__Cleaning up brew__
```shell
brew bundle dump # Writes all installed casks/formulae/taps to Brewfile
brew bundle --force cleanup # Removes all dependencies not listed in Brewfile
```

### Hugo

__Build with drafts__
```shell
hugo -D serve
```


