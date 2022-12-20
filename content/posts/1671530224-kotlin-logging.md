+++ 
date = 2022-12-20T09:57:16Z
title = "Kotlin Logging with SLF4J and Logback"
description = "Simple instructions to setup Kotlin Logging"
slug = "" 
tags = ["kotlin", "logging", "javafx"]
categories = ["til"]
externalLink = ""
series = []
+++

Add depedencies in `pom.xml` or `gradle` file

```xml
<dependency>
    <groupId>io.github.microutils</groupId>
    <artifactId>kotlin-logging-jvm</artifactId>
    <version>${kotlin-logging-jvm.version}</version>
</dependency>
<dependency>
    <groupId>ch.qos.logback</groupId>
    <artifactId>logback-classic</artifactId>
    <version>${logback-classic.version}</version>
</dependency>
```

Configure `logback.xml` file in `src/main/resources/logback.xml`.
The following file configures a File appender.
It logs it in a file under `$HOME/.gptfx/application.log` as it is used for a `JavaFX` application.

```xml
<configuration>
    <appender name="FILE" class="ch.qos.logback.core.FileAppender">
        <file>${user.home}/.gptfx/application.log</file>
        <encoder>
            <pattern>%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
        </encoder>
    </appender>

    <root level="debug">
        <appender-ref ref="FILE"/>
    </root>
</configuration>
```

If the project is using [Java Modules](https://www.oracle.com/uk/corporate/features/understanding-java-9-modules.html) then add the following two lines to grant access to required apis.

```properties
requires org.slf4j;
requires io.github.microutils.kotlinlogging;
```

That is all for setup.
Now we can use it by importing `mu.KotlinLogging` at the top level

```kotlin
import mu.KotlinLogging
```

Then using it where needed

```kotlin
logger.debug { "JSON Request: $requestBody" }
```

The output will be something like this

```text
 cat ~/.gptfx/application.log 
09:44:57.007 [pool-2-thread-1] DEBUG com.github.namuan.gptfx.GptApi - JSON Request: {"model":"text-davinci-003","prompt":"I have a document with a number of lines like the following `Page 41` where we have Page followed by a number. Can you show me how to remove it by using a command line tool?","temperature":0.1,"max_tokens":300,"top_p":1.0,"stream":false}
```
