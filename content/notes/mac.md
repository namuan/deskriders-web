---
title: "Mac (Apps/Tools/Tips and Tricks)"
date: 2021-12-19T15:46:00Z
---

### Apps

#### Screen Drawing

Found [quickdraw](https://github.com/maxchuquimia/quickdraw) which is an app for drawing over the screen.
Unfortunately, it doesn't seem to provide any packages, and I'm unable to build it locally.
A similar application which is quite good is [Pensela](https://github.com/weiameili/Pensela).

![](/images/2021/12/pensela.png)

#### Command Line Tools

* ImageMagick Resize a bunch of images using ImageMagick__

```bash
find ./static -name '*.png' | while read line; do convert -resize 1280x1280 $line $line; done
```

* jq: Length of array

```sh
$ echo '["123", "567", "abc"]' | jq '. | length'
```

* Shell: Pass contents of clipboard as file descriptor. It'll work with apps expecting file argument.

```sh
$ command <(pbpaste)
```

* Convert: Resize image

```
$ convert -quality 75% -resize 40x40 twitter.png twitter-icn.png
```

### Homebrew

__Updating packages___
```shell
brew update
```

### Hugo

__Build with drafts__
```shell
hugo -D serve
```


