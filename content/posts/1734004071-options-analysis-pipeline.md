+++ 
date = 2024-12-12T11:47:51Z
title = "Analysing a very simple Short Straddle strategy"
description = "Learn how to import OptionsDX data into an SQLite database, simulate a simple short straddle strategy, and analyze the results using SQL and a Dash application."
slug = "" 
tags = ["options", "trading", "data analysis", "backtesting"]
categories = ["Trading", "Data Analysis", "Python"]
externalLink = ""
series = []
+++

## Gather data

The Options data is retrieved from [optionsdx](https://www.optionsdx.com).
This page documents the [field definitions](https://www.optionsdx.com/option-chain-field-definitions/)

The downloaded files will be zipped, so extract them into a single directory. 
It'll look something like this:

![images/2024/12/12/1734006103-1.png](/images/2024/12/12/1734006103-1.png)

## Import data 

Use the [optionsdx-data-importer.py](https://github.com/namuan/trading-utils/blob/main/optionsdx-data-importer.py) script to import all the data in an SQLite database

```shell
$ uvr optionsdx-data-importer.py --input $(pwd)/data/spy_eod --output data/spy_eod.db -v
```

The finished database will have an `options_data` table with all the data from the downloaded files.

![images/2024/12/12/1734006103-2.png](/images/2024/12/12/1734006103-2.png)

## Simple Straddle Strategy

A simple short straddle strategy is provided where a new straddle is placed every day with 7 DTE.
The straddle is not managed, and we calculate the final price after 7 DTE as the closing price.

Run the [options-straddle-simple.py](https://github.com/namuan/trading-utils/blob/main/options-straddle-simple.py) script to simulate the strategy.

```shell
$ uvr options-straddle-simple.py --db-path data/spy_eod.db --dte 7
```

It'll update the same database with two more tables.

![images/2024/12/12/1734006103-3.png](/images/2024/12/12/1734006103-3.png)

The `trades` table contains each trade with opening and closing premium.
The `trade_history` table contains the trade period and daily premium prices for the selected strike.

## Reporting

There are a couple of ways to analyse trade data.
You can directly run SQL query against the database. 

Here is an SQL query to report the monthly premium difference (premium collected at open - paid back at close)

```sql
SELECT
    STRFTIME('%Y-%m', Date) AS Month,
    SUM(PremiumCaptured) AS TotalPremiumCaptured,
    SUM(ClosingPremium) AS TotalClosingPremium,
    SUM(PremiumCaptured - ClosingPremium) AS TotalPremiumDifference
FROM trades
GROUP BY Month
ORDER BY Month;
```

Quickly visualising the data with DataGrip

![images/2024/12/12/1734006103-4.png](/images/2024/12/12/1734006103-4.png)

The other way is more interactive and takes the user through the journey of each individual trade.
It is an application built with the [dash framework](https://dash.plotly.com)

Run the [options-straddle-simple-report.py](https://github.com/namuan/trading-utils/blob/main/options-straddle-simple-report.py) script to start the application.

```shell
uvr options-straddle-simple-report.py --database data/spy_eod.db --weeks 4            
```

Once started, you can click on the link displayed in the console.
You can visit [this link](http://127.0.0.1:8050/) assuming that it is running on the default port.

![images/2024/12/12/1734006103-5.png](/images/2024/12/12/1734006103-5.png)

The chart is interactive when running, so select different trades or click on highlighted dots to see data at the point.

You can also cycle through trades automatically by clicking on the **Start Auto Cycle** button.

![images/2024/12/options-trade-analysis-auto-cycle.gif](/images/2024/12/options-trade-analysis-auto-cycle.gif)
