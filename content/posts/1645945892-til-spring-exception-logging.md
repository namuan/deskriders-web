+++ 
date = 2022-02-27T06:51:10
title = "TIL :: Log Exceptions on a single line with Spring Boot"
description = "Different ways to log exceptions on a single line to make it work better with log aggregation services"
tags = ["java", "logging", "springboot"]
categories = ["til"]
externalLink = ""
series = []
+++

This can go in the `application.properties` file.

```ini
# Single line. Full stack trace will be captured in a single line
logging.exception-conversion-word=%replace(%wEx){'\n','\u2028'}%nopex

# Truncated Single line. Only the exception message will be captured in a single line
logging.exception-conversion-word=%replace(%wEx{short}){'\n','\u2028'}%nopex

# Truncated. Default formatting but only capturing a single line
logging.exception-conversion-word=%wEx{short}
```

This works if you don't override `logging.pattern.console` as the default `logging.pattern.console` allows you to use `logging.exception-converstion-word`

![Image](/images/2022/02/27/498904421940864.png)

If you need to only filter out certain packages from exception stack trace.

```ini
logging.pattern.console="[%d{yyyy-MM-dd HH:mm:ss.SSS}] [%5level] [${spring.zipkin.service.name:${spring.application.name:-}},%X{X-B3-TraceId:-},%X{X-B3-SpanId:-}] [%15.15t] [%-40.40logger{39}] - %m%n%rEx{full,
                   java.lang.reflect.Method,
                   org.apache.catalina,
                   org.springframework.aop,
                   org.springframework.security,
                   org.springframework.transaction,
                   org.springframework.web,
                   org.springframework.cglib,
                   feign,
                   com.netflix.hystrix,
                   rx.internal,
                   rx.Observable,
                   com.google.gson.internal,
                   java.util.concurrent,
                   sun.reflect,
                   net.sf.cglib,
                   ByCGLIB
                   }"
```

Or this ☝ can be applied with `logging.exception-conversion-word`

If you are using `logback.xml` then here is an example config. The key part is in `configuration > appender > encoder > pattern`

```xml
<configuration>
    <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>%d{HH:mm:ss.SSS} | %-5level | %thread | %logger{1} | %m%n%rEx{full,
                java.lang.reflect.Method,
                org.apache.catalina,
                org.springframework.aop,
                org.springframework.security,
                org.springframework.transaction,
                org.springframework.web,
                org.springframework.cglib,
                feign,
                com.netflix.hystrix,
                rx.internal,
                rx.Observable,
                com.google.gson.internal,
                sun.reflect,
                net.sf.cglib,
                ByCGLIB
                }
            </pattern>
        </encoder>
    </appender>
    <appender name="FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <encoder>
            <Pattern>${FILE_LOG_PATTERN}</Pattern>
        </encoder>
        <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
            <!-- rollover daily -->
            <fileNamePattern>${LOG_FILE}.%d{yyyy-MM-dd}.log</fileNamePattern>
            <!-- keep 7 days' worth of history in case AWS CloudWatch has problems capturing -->
            <maxHistory>7</maxHistory>
        </rollingPolicy>
    </appender>

    <root level="INFO">
        <appender-ref ref="STDOUT"/>
        <appender-ref ref="FILE"/>
    </root>

</configuration>
```

#### Reference

[https://logback.qos.ch/manual/layouts.html](https://logback.qos.ch/manual/layouts.html)
