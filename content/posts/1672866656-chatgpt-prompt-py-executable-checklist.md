+++
date = 2023-01-04T21:10:56Z
title = "ChatGPT prompt for generating steps and workflow using py-executable-checklist"
description = "Prompt for generating Python code"
slug = "" 
tags = ["prompt", "checklist", "python"]
categories = ["chatgpt"]
externalLink = ""
series = []
+++

### First Step: Generating each step one at a time

```text
I'm writing a Python application which defines a workflow as a series of steps defined by a class for each step.
Don't write any explanations.
Don't write the workflow function

DoSomething is a step in the workflow and is defined as

class DoSomething(WorkflowBase):
"""
Go to this page
Copy the command
Run the command
Copy the output and paste it into the email
"""
username: str

    def execute(self):
        logging.info(f"Hello {self.username}")

        # output
        return {"greetings": f"Hello {self.username}"}

Where username is the input to this workflow and execute method implements the workflow.
Each step can return some state by returning a dictionary of key value pairs.

Based on the above description, can you write a workflow for the following scenario

* Given an input file path to an ogg audio file, convert it to mp3 and return the mp3 file path from step

Using the above step definition syntax, implement the following step
Don't write any explanations.
Don't write the workflow function

* Given the path to mp3 file, Play the mp3 file and return nothing
```

### Second step

```text

Given the above steps, can you refined the following functions with the list of steps replacing DoSomething

def workflow():
    return [
        DoSomething,
    ]
```
