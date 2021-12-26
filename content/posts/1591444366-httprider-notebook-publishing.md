+++ 
draft = false
date = 2020-06-06T11:53:52
title = "Publishing Notebooks with HttpRider"
description = "Design document for implementing notebooks with HttpRider"
slug = ""
tags = ["document", "architecture"]
externalLink = ""
series = ["httprider"]
+++

Preliminary design document for implementing notebooks with HttpRider.

This feature enables the user to publish interactive API notebooks.
These interactive API notebooks can be used to document a scenario where an individual API call doesn't make sense without the context around it.

#### Features

[] Publish API call description in Markdown format

[] Publish API call as curl commands

[] Allow user of the notebook to run curl commands interactively

[] Track the response of the commands and use the output to chain other calls

[] A Notebook can only be published from the HttpRider application

[] A Notebook can be shared publicly using a unique URL

[] A Notebook can be shared with another user

[] A Notebook can be shared with another team

#### How it works

There will be three different entities involved in a usual use case. The desktop application [App] which talks to the server [Server] and the client [Client] to render the notebook

```
[App] Generates q unique identifier to identify the app (So that we can link the notebooks with the App) and it can be used later to link the user to the notebooks and the App
[App] Button to publish the selected API calls
[App] Opens up a modal dialog box to show preview
[App] User is allowed to update description text or the curl commands in the preview window
[App] User click on the Send button
[App] POST /notebooks along with the content of the API Calls
[Server] Receives the POST request and generates a unique identifier of the notebook after saving the request in the database
[Server] Returns the Location (Header) of the notebook with HTTP 201
[App] Validates that the response code is HTTP 201 and display the generated link to the user
[App] User clicks on the link
[App] Opens up the URL in the default browser
[Client] Handles the Notebook URL and extract the unique identifier
[Client] Makes a call to the server to get the notebook data
[Client] Renders the notebook along with the buttons to run curl commands
[Client] User clicks on the button to run curl command
[Client] Validates that all the required variables are provided for running the curl command
[Client] If any variable is missing then opens up a modal form to ask for the missing variables
[Client] Once pre-condition is satisfied, it packages up the curl command and send it to server
[Server] Receives the command and run it against the target
[Server] Receives the response back from the target and return it back to the client
[Client] Receives the response from the server and renders in below the curl command
[Client] Extracts variables from the response and updates subsequence curl commands with the variable values
```

#### Data Model

We have three different entities

Notebook

|   Fields    |                                                                                      |
| ----------- | ------------------------------------------------------------------------------------ |
| id          | unique identifier                                                                    |
| publisher   | user_id                                                                              |
| unique_link | url safe random identifier                                                           |
| shared_with | List of { id, type } where id the user or team identifier and type in [USER, TEAM] |
|             |                                                                                      |

User

|   Fields   |                                  |
| ---------- | -------------------------------- |
| id         | user unique identifier          |
| email      | user email                       |
| invited_by | user identifier for the invitee |
|            |                                  |
|            |                                  |

Team

|  Fields   |                                                                                     |
| --------- | ----------------------------------------------------------------------------------- |
| id        | unique identifier                                                                   |
| user_list | List of {id, role} where id is user unique identifier and role in [ADMIN, MEMBER] |
|           |                                                                                     |
|           |                                                                                     |
|           |                                                                                     |