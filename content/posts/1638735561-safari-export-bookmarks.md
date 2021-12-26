+++
date = 2021-12-05T20:19:36Z
title = "Export Reading list from Safari"
description = "Steps to export your Safari reading list to a bookmarks file"
slug = "" 
tags = ["safari"]
externalLink = ""
series = ["tooltips"]
+++

1. open ~/Library/Safari

2. Copy the Safari bookmarks file to your desktop.

    ![](/images/1638735561-safari-export-bookmarks.png)

3. Then run the following command to get the list of links

```
plutil -convert xml1 -o - Bookmarks.plist | grep -E  -o '<string>http[s]{0,1}://.*</string>' | grep -v icloud | sed -E 's/<\/{0,1}string>//g'
```

__References__

https://apple.stackexchange.com/questions/24864/is-it-possible-to-export-safaris-reading-list-on-safari-5-1#62431
