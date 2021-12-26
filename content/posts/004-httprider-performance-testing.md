+++ 
date = 2019-11-16T16:24:01Z
title = "Performance testing with HttpRider"
description = ""
slug = "" 
tags = ["testing", "api", "python"]
externalLink = ""
series = ["httprider"]
+++

The title is a bit misleading as [HttpRider](https://github.com/namuan/http-rider) can't run performance tests (as of now), however it can be used to generate performance tests using a couple of different approach.

#### Slow cooker:

[SlowCooker](https://github.com/BuoyantIO/slow_cooker) is a command line tool for load testing. [Here](https://buoyant.io/2016/12/10/slow-cooker-load-testing-for-tough-software/) is an excellent blog post about the background and difference from other similar tools. 

![](/images/004/httprider_slowcooker.gif)

Generating code to run slow cooker is as simple as selecting an API call and click on the export button to generate code. Along with the command, you can find brief documentation on command line arguments and output format.

Although tools like slow\_cooker, ab are good at testing endpoints independently but they fall short if we need to chain few requests or generate data dynamically. 

This is where it is useful to have [JMeter](https://jmeter.apache.org) or [Locust.io](https://locust.io) where you can create a complex user journey and chain requests. 

#### Locust.io:

Here is a small demo of generating and running performance tests with Locust.io.

{{< youtube 7zqcYmZIdVs >}}