+++
date = 2021-12-26T09:56:42
title = "[SaaS Idea] Markdown to ... converter"
description = "Online service to convert Markdown to PDF / Confluence / Word / Google Docs / HTML"
slug = ""
tags = ["ideas"]
externalLink = ""
series = ["ideas"]
+++
        
> Summary: Online service to convert Markdown to PDF / Confluence / Word / Google Docs / HTML etc

### Release 1.0:

Feature: Convert Markdown to Confluence

    Scenario: Successfully post Markdown document
        Given: a Markdown document
        When: JD posts the document
        Then: I accept the document
        And: Return a unique identifier

    Scenario: Successfully convert Markdown document
        Given: a Markdown document
        When: JD posts the document
        Then: I convert the document to Confluence
        And: Return a unique link to download converted document

## Technology

[] Subdomain - markdown.example.com
[] AWS Lambda/API Gateway using serverless framework
[] Python Flask

#### Sequence Flow

<!---
```puml
@startuml

actor User
participant Service
participant APIG
participant Collector
participant Processor
participant Downloader
database S3
database DynamoDB

User -> Service: Upload Markdown document
Service -> APIG: Received HTTP event
APIG -> Collector: Triggers lambda
Collector -> Collector: Generate unique identifier
Collector -> DynamoDB: Save a new entity
note right of Collector
    status=InProgress
end note
Collector -> S3: Uploads Markdown document
Collector -> APIG: Unique identifier
S3 -> Processor: Triggers lambda
Processor -> Processor: Lookup DynamoDB for entity
Processor -> Processor: Convert Markdown document \n -> target format
Processor -> S3: Upload converted document
Processor -> DynamoDB: Update entity
note right of Processor
    status=Complete
    link=S3 converted document
end note
APIG -> Downloader: Check status using Unique identifier
Downloader -> DynamoDB: Check if status=Complete
alt Status=Complete
    Downloader -> APIG: Return download link
else Status!=Complete
    Downloader -> APIG: Wait for few seconds before retrying
end

@enduml
```
--->
![](/images/2021/12/26/tmpa37jr0ko.png)