+++ 
draft = false
date = 2020-05-14T23:45:43+01:00
title = "Using EasyRandom with Spring Framework"
description = "EasyRandom is an extremely useful library to generate Java beans with random data"
slug = "" 
tags = ["java", "tips"]
categories = ["java"]
externalLink = ""
series = []
+++

Tired of creating objects in tests. Try using EasyRandom library. Here is how easily you can add it to a Spring Java project

#### Step 1: Add gradle/maven dependency

https://mvnrepository.com/artifact/org.jeasy/easy-random

![](/images/20200514225404481_20190134.png)

#### Step 2: Declare it in test

![](/images/20200514230728850_1337135243.png)

#### Step 3: Use it to generate random data objects

![](/images/20200514230800345_1963146893.png)


#### Step 4: 😍

![](/images/20200514230639150_1516619298.png)

#### Tips:

#### Random initial seed
In the default setup, EasyRandom uses a default seed value to generate randam data.
Although it is quite simple to initiate EasyRandom with a random seed.

![](/images/20200514231839075_671078143.png)

#### Enforcing javax.validation rules:

If an object is using javax.validation then there is an extension which enforces those rules when generating random objects.

Include https://github.com/j-easy/easy-random/wiki/bean-validation-support

![](/images/20200514232418213_226235357.png)
![](/images/20200514232450020_1291589909.png)


