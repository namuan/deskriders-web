+++
date = 2021-12-26T09:50:56
title = "Implementing Features with Microservices Architecture"
description = ""
slug = ""
tags = ["ideas"]
externalLink = ""
series = ["ideas"]
+++
        
An ongoing thought process on how to help with generating code when working on a microservices based architecture.

In most organisations I worked with, the usual microservices development model is *roughly* divided into two main parts.

### 1. Common Functionality

We can classify the following responsibilities as common across multiple micro services

* Build and deployment pipeline
* Logging destination and output
* Environment Configuration
* Publishing metrics
* Tracing across multiple services
* API request/response formats
* Handling Idempotency where applicable

All of these will feed into different architectural concerns where it is important to have consistency across multiple microservices. Hopefully these will be defined once and rarely change over time.

### 2. Domain Specific Functionality

In addition to the common functionality above, the following things are usually required when adding a new feature.

* Define API route
* Define API request input parameters
* Define/Validate API input parameters
* Define schemas for messaging
* Call external services. It could be over JSON/SOAP based webservices or Kafka/JMS for asynchronous processing
* Define schemas/migration scripts for database entities
* Call database for CRUD operations
* Format successful/error API responses
* Unit tests
* Component test with embedded databases and mocked stubs
* Generating API documentation

A common implementation of a use case is defined as a sequence diagram here.

<!---
```puml
@startuml

title Adding Employee to Employee Directory

participant User as user
participant AddEmployeeController as controller
participant AddEmployeeApiRequestValidator as validator
participant AddEmployeeService as service
participant AddEmployeeMapper as mapper
participant Repository as db
participant Kafka as q
participant FeignClient as downstream

user -> controller: POST /employees
note right of user
  **Header**
  Content-Type: application/json
  **Payload**
  {
    "name": "Something",
    "age": 34,
    "role": "Software Engineer"
  }
end note
controller -> validator: validateRequest(AddEmployeeApiRequest)
note right of controller
    **class AddEmployeeApiRequest**
    String name<font color="red">*</font>
    int age
end note
validator -> controller: [void or ConstraintViolationException]
controller -> service: addEmployee(AddEmployeeApiRequest)
service -> mapper: convertObject(AddEmployeeApiRequest)
note right of service
    **class DownstreamApiRequest**
    String name<font color="red">*</font>
end note
mapper -> service: [DownstreamApiRequest]
service -> downstream: PUT /v1/employees
note right of service
    **Header**
    Content-Type: application/json
    **Payload**
    {
      "name": "John Doe"
    }
end note
downstream -> service: HTTP 200
note right of downstream
    **Header**
    Content-Type: application/json
    **Response Payload**
    {
      "id": "{uuid}"
    }
end note
service -> db: save(EmployeeEntity)
note right of service
    **class EmployeeEntity[Employee]**
    UUID id [id/@Id]
    UUID employeeId [employee_id/string]
    String employeeName [employee_name/string]
    int employeeAge [employee_age/int]
end note
db -> service: [?] 
service -> q: SEND to TOPIC employee-added-v1
note right of q
    **Record: EmployeeAdded**
    **Field**
    String name<font color="red">*</font>
    int age
    String employeeId<font color="red">*</font>
end note
@enduml
```
--->
![](/images/2021/12/26/tmp5x1i5mes.png)
