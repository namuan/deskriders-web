+++
date = 2024-05-04T13:08:43+01:00
title = "Tracking Stocks in Google Sheet"
description = "Monitor your investment portfolio by integrating real-time stock market data into your Google Sheet"
slug = "" 
tags = ["trading", "sheets"]
categories = []
externalLink = ""
series = []
+++

### Generate CSV reports

```shell
$ ./generate-csv-reports.sh 2>&1 | grep "Exporting report"
```

### Combine all reports

```shell
$ python3 combine-all-csvs.py                                                                                   
```

### Paste into Google Sheet

![image](/images/2024/05/05/1714934552.png)

### Re-arrange and apply formulas

```text
Last Close: =GOOGLEFINANCE(C3,"price")
Current Code: =G3*E3
TV Link: =HYPERLINK(CONCATENATE("https://www.tradingview.com/chart/?symbol=", C3), C3)
Chart: =sparkline(googlefinance(C3,"price",today()-30,today()))
Profit Loss: =I3-H3
```
