+++ 
date = 2019-10-27T11:30:15Z
title = "Generating Runscope monitoring tests with HttpRider"
description = ""
slug = "" 
tags = ["monitoring", "python", "api"]
externalLink = ""
series = ["httprider"]
+++

[Runscope](https://www.runscope.com) (Now Part of [BlazeMeter](https://www.blazemeter.com)) is a well known service for API Monitoring. This post covers generating Runscope monitoring tests from [HttpRider](https://github.com/namuan/http-rider).

We start with API definitions in HttpRider, make sure you run them at least once as some of the exporters use the data from the response.

![](/images/002/httprider_runscope_1.png)

Along with API definitions, it also generates [Runscope environments](https://www.runscope.com/docs/api-testing/environments/) with placeholders for any variables used from environment.

![](/images/002/httprider_runscope_2.png)

Once the tests have successfully finished, click on the export/export all button to display the code generator. 

Select Runscope from the dropdown list to see generated code in [Runscope API tests format](https://www.runscope.com/docs/api-testing/importing/#radar-import).

![](/images/002/httprider_runscope_3.png)

Copy the code and save it in a json which we'll use to import.

![](/images/002/httprider_runscope_4.png)

Next, we'll import the json file in Runscope

![](/images/002/httprider_runscope_5.png)

![](/images/002/httprider_runscope_6.png)

If everything goes well, Runscope will import the tests including any defined environments.

![](/images/002/httprider_runscope_7.png)

You can select the appropriate environment and select an appropriate location to run the tests from.

![](/images/002/httprider_runscope_8.png)

You'll notice that variables are converted into "Initial variables" for an environment and referenced in request header/body where required. These variables can also be set in javascript to use a dynamic value everytime a test runs. See [Dynamic Request Data](https://www.runscope.com/docs/api-testing/variables/) for more info.

![](/images/002/httprider_runscope_9.png)

Finally, save and run the tests to see the results. If the backend API is up and running, you should see a ✅ along with the assertions.

![](/images/002/httprider_runscope_10.png)

And that's all for now 🎉.

> [HttpRider](https://www.httprider.com/) is open source so please [try it out](https://www.httprider.com/docs/getting-started/installation/). There is a [sample](https://github.com/namuan/http-rider/tree/master/sample) included in the project to quickly load a few APIs running against httpbin.org.

{{< youtube YNE12-YqiLc >}}