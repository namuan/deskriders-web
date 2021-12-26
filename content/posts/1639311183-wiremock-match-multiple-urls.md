+++ 
date = 2021-12-12T12:13:25Z
title = "Wiremock: How to match multiple urls in a single mapping"
description = "Example JSON mapping to match multiple urls"
slug = "" 
tags = ["wiremock", "json", "mapping"]
externalLink = ""
series = ["tooltips"]
+++

[Wiremock](http://wiremock.org/) is a tool to mock HTTP APIs.
You can set up Stubs in Wiremock by using their API or by calling the admin API over HTTP. 
Usually it is used as part of a test suite but here I'm running the [standalone](http://wiremock.org/docs/running-standalone/) Wiremock server.

Once the jar file is downloaded, you can start the server by running the following command:

```shell
java -jar wiremock-jre8-standalone-2.32.0.jar
```

Here we are setting multiple URLs to match in a single mapping.

```shell
cat << EOF | http POST http://localhost:8080/__admin/mappings
{
    "request": {
        "method": "GET",
        "urlPattern": "/health|/actuator/health"
    },
    "response": {
        "status": 200,
        "headers" : {
            "Content-Type" : "application/json"
        },
        "body": "{\"status\": \"UP\"}"
    }
}
EOF
```

Once it is set, you can test the mapping by calling the URL:

```shell
http GET http://localhost:8080/health
HTTP/1.1 200 OK
Content-Encoding: gzip
Content-Type: application/json
Matched-Stub-Id: 1641b44a-5f4b-48f9-bbe6-e7f81054a064
Transfer-Encoding: chunked
Vary: Accept-Encoding, User-Agent

{
    "status": "UP"
}
```

Or by calling the alternative URL:

```shell
http GET http://localhost:8080/actuator/health
HTTP/1.1 200 OK
Content-Encoding: gzip
Content-Type: application/json
Matched-Stub-Id: 1641b44a-5f4b-48f9-bbe6-e7f81054a064
Transfer-Encoding: chunked
Vary: Accept-Encoding, User-Agent

{
    "status": "UP"
}
```
