+++ 
date = 2019-10-28T11:30:47Z
title = "Generating BDD tests with HttpRider"
description = ""
slug = "" 
tags = ["testing", "api", "python"]
externalLink = ""
series = ["httprider"]
+++

In this post, we'll see how we can easily generate BDD tests with HttpRider. 

Instead of writing the code behind the REST api calls, we'll use an open source framework called [Apickli](https://github.com/apickli/apickli) to do the heavy lifting. Apickli is based on cucumber.js and defines a number of pre-built [Gherkin expressions](https://github.com/apickli/apickli#gherkin-expressions). 

I've also created a [sample project](https://github.com/namuan/apickli_functional_tests) using Apicki framework to make it easy to get it up and running.

Let's start with a few API calls using the [sample database](https://github.com/namuan/http-rider/tree/master/sample) provided with source. Once it is loaded, please make sure that you run all the APIs at least once as some of the exporters use the response to generate code.  
  
 ![](https://deskriders.dev/media/posts/13/apickli_1.png)

Now, click on Export/Export All to open up code generator.

![](/images/003/apicli_2.png)

Select Apickli Tests from the drop down menu to see the BDD generated code. 

![](/images/003/apickli_3.png)

If you don't have a project setup, then you can clone the [test project](https://github.com/namuan/apickli_functional_tests) and replace the contents of [Functional.feature](https://github.com/namuan/apickli_functional_tests/blob/master/tests/Functional.feature) file with the exported code.

Run `npm i` to install the dependencies and then `npm run all` to run all the included scenarios.

![](/images/003/apickli_4.png)

You can also view the generated report by running `npm run report` which should generate the HTML report in the `report` folder. 

![](/images/003/apickli_5.png)

> [HttpRider](https://www.httprider.com/ "HttpRider") is an open source cross platform desktop client for working with JSON APIs. Please checkout the [features](https://github.com/namuan/http-rider#features) on Github.

See the demo video to generate BDD tests using HttpRider and Apickli.

{{< youtube mGiF0DfLaSU >}}