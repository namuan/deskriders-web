+++
date = 2023-01-04T21:14:23Z
title = "ChatGPT Prompt for generating py-executable-checklist step"
description = "Write nice clean python code for the step class"
slug = "" 
tags = ["prompt", "checklist", "step"]
categories = ["chatgpt"]
externalLink = ""
series = []
+++

```text
[Command]

Create a complete, working, and VERY efficient Python code. Do NOT send me the explanations of how the function works, you need to implement it yourself and ONLY send me the code WITHIN CODE BLOCKS ONLY. Your answer NEEDS TO start with the imports (if any), and then directly follow with the implementation as described by the [Template] below.
The step name is defined in the [Step name] section and description in the [Task definition] section

Here is the [template] that you will need to work with. Any code you write will be inside the execute method

In this template, `username` is the input to this class as defined in the [Step parameters] section.
The return value will be a dictionary of the items as defined in the [Step output] section

[Template]

class DoSomething(WorkflowBase):
"""
Do something description
"""

    username: str

    def execute(self) -> dict:
        logging.info("Number of pages: %s", self.pdf_properties["pages"])

        # output
        return {"todo": "Next Step"}


[Additional specifications]

You HAVE to split the execute function into multiple functions: A function should NEVER be more than 10 lines of code.

You need to add comments inside your code when necessary; ***DO NOT bloat the code with comments, only add helpful ones***.

If you call additional functions within your code, you HAVE to declare and implement them. You CANNOT ASSUME that functions are created, you HAVE to implement them FULLY.

[Step name]

ConvertPDFToImages

[Step parameters]

The main function will take the following parameters in the format [variable name]: [variable type]

input_pdf_path: Path
pdf_pages: int

[Step output]

The main function will output the following inside the dictionary

pdf_images_page: Path


[Task definition]

Given a path to a PDF File, it will extract the PDF file naem
It will create a directory called 'OutputDir/dr-doc-search/<pdf-file-name>/images' under the home directory.
It will use ImageMagick convert utility to generate images for each page of the input PDF.
Here are the additional arguments to use with convert command
-density 150 -trim -background white -alpha remove -quality 100 -sharpen 0x1.0
The output will the directory where the images were saved
```