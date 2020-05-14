+++ 
draft = false
date = 2020-05-08T15:00:06+01:00
title = "Gradle custom task for selectively running tests"
description = "how do I define contract tests which can be run on-demand from Gradle while ignoring them from unit test runs?"
slug = "" 
tags = ["java", "gradle"]
categories = ["java"]
externalLink = ""
series = []
+++

*Q: How do I define contract tests which can be run on-demand from Gradle while ignoring them from unit test runs?*

Here, I'll add a test which is ignored when running `./gradlew test` but it can be triggered when needed (eg. from a separate Jenkins Job).

The current directory structure look this

![](/images/20200508151905944_642229617.png)


The first step is to exclude all the tests under contracts/

```groovy
test {
	...

	exclude('**/contracts/*.*')
}
```

Then we'll define another Gradle task so that contract tests can be executed on demand

```groovy
task contractTests(type: Test, group: 'verification') {
    ...

    include('**/contracts/*.*')
}
```

Once you have it setup

Run all tests which will exclude any contract tests

```
./gradlew test
```

And at the same time, we can run just contract tests

```
./gradlew contractTests
```

🎉

