+++ 
date = 2025-05-31T12:00:33+01:00
title = "Prompt Chain for Decomposing Tasks and Step-by-Step Implementation"
description = "A series of example prompts to implement a feature step by step"
slug = "" 
tags = ["prompts"]
categories = ["programming", "development"]
externalLink = ""
series = []
+++

### Initial Prompt

> Provide an overall solution for the problem stated at the end.
> Don't generate code.
> Describe the solution and break it down into a task list.
> We will refer to this task list as our master plan.
> Reply succinctly and do not add anything not required for the solution.
> Each task in the task list should be a single line.
>
> Problem:
> I want to develop a Carousel component in React using TypeScript.

### Generate High-Level Structure

> Rewrite the master plan, this time with detailed component names, methods, and props.
> Use Mermaid JS to display components and their methods.
> Generate a Class Diagram.
> Generate a Component Diagram.
> Generate a Sequence Diagram.
>
> Create an HTML page with embedded Mermaid JS.
>
> Do not generate code.

### Implementation

> I'd like to implement these steps using Lean methodology.
> Each step should include runnable code with an example test.
> Provide the example test first, followed by the implementation.
> Generate tests using the Jest framework.
>
> Technologies:
> React, Jest, TypeScript, Styled Components
>
> As instructed previously:
> If a change is required in existing code, identify all methods where changes are needed.
> Display the output as follows:
> List all imports first if needed.
> Then, for each method:
> Display the method name along with the class name if the method belongs to a class.
> Display the full source code of the method, even if the change is minor.
> If the method belongs to a class, indent it to help the user paste it directly into the IDE.
> Do not add any explanation at the end. Keep it as concise as possible.
> Always answer in English.
>
> Example when imports are not needed and the change is in a method belonging to a class:
>
> Class: Foo
> Method: Bar
>
> ```
> Code
> ```
>
> Example when imports are not needed and the change is in a method that doesn't belong to a class:
>
> Class: None
> Method: Bar
>
> ```
> Code
> ```
>
> Once the task is complete, move to the next task and implement it using the above instructions.
>
**We can also propose the next task to implement and wait for confirmation before starting on the next task.**