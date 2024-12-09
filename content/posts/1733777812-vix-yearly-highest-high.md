+++ 
date = 2024-12-09T20:56:52Z
title = "VIX yearly highest values over the last 20 years"
description = "Find the yearly highest value of VIX"
slug = "" 
tags = ["vix", "investment"]
categories = ["research"]
externalLink = ""
series = []
+++

Started as a question from this [tweet](https://x.com/ksidiii/status/1866088473985245220?s=12)

I downloaded `^VIX` data from Yahoo Finance using this script.

https://github.com/namuan/trading-utils/blob/main/download_stocks_ohlcv.py

```shell
uvr download_stocks_ohlcv.py --tickers ^VIX --back-period-in-years 20
```

Assuming the output data is download in a CSV file `output/\^VIX.csv`

I imported the CSV data in an Sqlite3 database

```shell
$ sqlite3 vix.db
```

In the Sqlite3 prompt

```sql
CREATE TABLE vix_prices (
    date TIMESTAMP,
    adj_close REAL,
    close REAL,
    high REAL,
    low REAL,
    open REAL,
    volume INTEGER
);
.mode csv
.import output/\^VIX.csv vix_prices
```

Now run this from the prompt to verify that data is imported successfully.

```sql
SELECT * FROM vix_prices LIMIT 5;
```

Then from the same prompt, we can generate a table in Markdown format

```sql
.mode list
.separator " | "
SELECT '| Year | Date | Highest Price |';
SELECT '|------|------|--------------|';
SELECT '| ' || strftime('%Y', date) || ' | ' || strftime('%Y-%m-%d', date) || ' | ' || ROUND(High, 2) || ' |'
FROM vix_prices
WHERE (strftime('%Y', date), High) IN (
    SELECT strftime('%Y', date), MAX(High)
    FROM vix_prices
    GROUP BY strftime('%Y', date)
)
ORDER BY date;
```

This is the formatted output from the above query 

| Year | Date       | Highest |
|------|------------|---------|
| 2004 | 2004-12-09 | 13.71   |
| 2005 | 2005-04-18 | 18.59   |
| 2006 | 2006-06-13 | 23.81   |
| 2007 | 2007-08-16 | 37.5    |
| 2008 | 2008-10-24 | 89.53   |
| 2009 | 2009-01-20 | 57.36   |
| 2010 | 2010-05-21 | 48.2    |
| 2011 | 2011-08-08 | 48.0    |
| 2012 | 2012-06-04 | 27.73   |
| 2013 | 2013-06-24 | 21.91   |
| 2014 | 2014-10-15 | 31.06   |
| 2015 | 2015-08-24 | 53.29   |
| 2016 | 2016-01-20 | 32.09   |
| 2017 | 2017-08-11 | 17.28   |
| 2018 | 2018-02-06 | 50.3    |
| 2019 | 2019-01-02 | 28.53   |
| 2020 | 2020-03-18 | 85.47   |
| 2021 | 2021-01-29 | 37.51   |
| 2022 | 2022-01-24 | 38.94   |
| 2023 | 2023-03-13 | 30.81   |
| 2024 | 2024-08-05 | 65.73   |
