+++
date = 2020-01-01T16:51:35Z
title = "Developing API exchange sharing service - Part I"
description = ""
slug = "" 
tags = ["serverless", "tutorial", "python"]
categories = ["tutorial"]
externalLink = ""
series = []
+++

In this series of articles, I'll go through my experience of building a simple Serverless API using [Flask](https://palletsprojects.com/p/flask/) python framework and deploying it on [AWS Lambda](https://aws.amazon.com/lambda/) and API gateway. 

This API is used from [HttpRider](https://github.com/namuan/http-rider) to save API exchanges (request+response). 

Here is a [sample page](https://printrider.bettercallbots.com/prints/9e4d91c5-4526-471f-8896-79543ccaeb6a) generated from HttpRider.


### Demo

![Quick Demo](/images/008/0148au5ftxy2fby8qufj.gif)

The service itself consists of two simple APIs.

#### POST /prints

Saves the HTML encoded in base64 in dynamo database. Once it is saved, it returns the URL of the shared document in the Location header of the response.

```
POST /prints
```
*Headers*
```
Content-Type: application/json
```

*Body*
```
{
    "document": "SHR0cFJpZGVy"
}

```

*Response*

```
HTTP 201
```

*Headers*
```
location: http://localhost:8080/prints/025000cf-14ba-421b-a000-d2d043d4d90b
```

#### GET /prints/{print-id}

This GET request uses the URL from the location header in the previous request and receives the HTML response with the document.

```
GET /prints/025000cf-14ba-421b-a000-d2d043d4d90b
```
*Headers*
```
Accept: text/html
```

*Response*

```
HTTP 200
```

*Headers*
```
content-type: text/html; charset=utf-8
```

*Body*
```
<!DOCTYPE html>
<html>
<head>
    <title>Deskriders :: API Print</title>
    <style>
       .... removed to save space ...
    </style>
</head>
<body>
<div>HttpRider</div>
</body>
</html>

```
In the next part, we will look at setting up a new Flask project and serverless framework configuration to deploy it to AWS Lambda.