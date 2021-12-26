---
title: "Random learning notes"
date: 2020-01-20T09:45:05Z
---

### Websites

* Simple but very useful website to format Markdown tables -> http://markdowntable.com

* Publishing blog/documentation using MKdocs -> https://github.com/tiangolo/dockerswarm.rocks

https://awslabs.github.io/smithy/quickstart.html
* Smithy is an interface definition language and set of tools that allows developers to build clients and servers in multiple languages.

* Alfred update script -> https://github.com/sballin/alfred-search-notes-app/blob/master/update.py

### Blog posts

* Side-projects on Google Cloud Run -> https://alexolivier.me/posts/deploy-container-stateless-cheap-google-cloud-run-serverless

* Lunr.js search on Hugo -> https://palant.info/2020/06/04/the-easier-way-to-use-lunr-search-with-hugo/

### Notes
* URI Encoding: How `:` becomes `%3A` using [Percent Encoding](https://en.wikipedia.org/wiki/Percent-encoding)

We start with finding the ASCII value of `:` which is `58`. 
See [ASCII table](https://theasciicode.com.ar/ascii-printable-characters/colon-ascii-code-58.html)

Convert 58 to binary using Short division by Two with Reminder. 
i.e. Divide the answer by 2 and keeping the reminder which will be the binary form.

```
58/2 = 29 => Reminder 0
29/2 = 14 => Reminder 1
14/2 = 7  => Reminder 0
7/2  = 3  => Reminder 1
3/2  = 1  => Reminder 1
1/2  = na => Reminder 1
```

So the binary form is `111010` if we line up all the reminders
Padding the output will make it `00111010`.

Convert the binary into two parts of 4 bits each.

`0011` `1010`

Using the following Hex table conversion, we map `0011` => 3 and `1010` to A which becomes `3A`. 

| Decimal | Binary | Hex |
|---------|--------|-----|
| 1       | 0001   | 1   |
| 2       | 0010   | 2   |
| 3       | 0011   | 3   |
| 4       | 0100   | 4   |
| 5       | 0101   | 5   |
| 6       | 0110   | 6   |
| 7       | 0111   | 7   |
| 8       | 1000   | 8   |
| 9       | 1001   | 9   |
| 10      | 1010   | A   |
| 11      | 1011   | B   |
| 12      | 1100   | C   |
| 13      | 1101   | D   |
| 14      | 1110   | E   |
| 15      | 1111   | F   |

The final part is to prefix it with `%` (which is the escape character) makes it `%3A`
