+++ 
date = 2019-08-26T08:32:55Z
title = "KubeRider :: Bundling MacOS release"
description = ""
slug = "" 
tags = ["kuberider", "packaging"]
externalLink = ""
series = []
+++

In this post, I'll go through what is involved in building a MacOS release package and publishing it on Github from TravisCI.

### Step 1: Application Icon 

Although it is probably quicker to find/generate a logo from an online service. I decided to create a simple logo to go through the process of creating and converting it in vector drawing.  
  
Here is what I ended up using the Paper app on iPad.

![](/images/006/kuberider_logo_image.png)

The next step is to convert it in vector which is easy once you managed to install Inkscape.

[![Logo Design](https://img.youtube.com/vi/5zgugMUlz58/0.jpg)](https://www.youtube.com/watch?v=5zgugMUlz58)

Now that the SVG file is exported, I have a helper script to generate iconset using Inkscape.

```
#!/usr/bin/env bash
  
inkscape="/Applications/Inkscape.app/Contents/Resources/bin/inkscape"
svg_file=$1
output_name=$2
  
set -e
test -d "$output_name.iconset" && rm -R "$output_name.iconset"
mkdir "$output_name.iconset"
$inkscape -z -e "$PWD/$output_name.iconset/icon_16x16.png" -w 16 -h 16 "$svg_file"
$inkscape -z -e "$PWD/$output_name.iconset/icon_16x16@2x.png" -w 32 -h 32 "$svg_file"
$inkscape -z -e "$PWD/$output_name.iconset/icon_32x32.png" -w 32 -h 32 "$svg_file"
$inkscape -z -e "$PWD/$output_name.iconset/icon_32x32@2x.png" -w 64 -h 64 "$svg_file"
$inkscape -z -e "$PWD/$output_name.iconset/icon_128x128.png" -w 128 -h 128 "$svg_file"
$inkscape -z -e "$PWD/$output_name.iconset/icon_128x128@2x.png" -w 256 -h 256 "$svg_file"
$inkscape -z -e "$PWD/$output_name.iconset/icon_256x256.png" -w 256 -h 256 "$svg_file"
$inkscape -z -e "$PWD/$output_name.iconset/icon_256x256@2x.png" -w 512 -h 512 "$svg_file"
$inkscape -z -e "$PWD/$output_name.iconset/icon_512x512.png" -w 512 -h 512 "$svg_file"
$inkscape -z -e "$PWD/$output_name.iconset/icon_512x512@2x.png" -w 1024 -h 1024 "$svg_file"
iconutil -c icns "$output_name.iconset"
rm -R "$output_name.iconset"
mv $output_name.icns packaging/data/icons/
  
$inkscape -z -e "$PWD/${output_name}/images/${output_name}.png" -w 512 -h 512 "$svg_file"
```

Then we simply run the above script providing it the path to the svg file

```
./mk-icns.sh `pwd`/kuberider/images/kuberider.svg kuberider
```

That generates an icon set and an image which will be used during package installation.

![](/images/006/kr_iconset_image.png)

### Step 2: Building an Apple Disk Image (dmg) file 

The [setup.py](https://github.com/namuan/kube-rider/blob/master/setup.py) uses [py2app](https://py2app.readthedocs.io/en/latest/) to generate an .app file for MacOS and [Node AppDmg](https://github.com/LinusU/node-appdmg) package to produce the DMG file.

### Step 3: Publishing from TravisCI to Github

The release pipeline is separated into two different Github repos so that I can control the release process. The [kube-rider-osx](https://github.com/namuan/kube-rider-osx) repo contains the [.travis.yml](https://github.com/namuan/kube-rider-osx/blob/master/.travis.yml) file to download the release and prepare the toolchain to generate and publish the release.

![](/images/006/kuberider_github_releases.png)

Once successfully built, TravisCI publishes the new release on Github

![](/images/006/travisci_release_publish.png)