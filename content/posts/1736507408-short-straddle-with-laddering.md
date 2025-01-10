+++ 
date = 2025-01-10T11:10:08Z
title = "Short Straddles with Laddering"
description = "What if we ladder contracts and compare it to different alternatives"
slug = ""
tags = ["options", "trading", "data analysis", "backtesting"]
categories = ["Trading", "Data Analysis", "Python"]
externalLink = ""
series = []
+++

**Short Straddles**

For e.g. Given that our account can trade 5 SPX contracts at once.

* We can either trade 1 contract every day - 5 different positions
* Or we can trade all 5 contracts at the same time in a single trade - 1 position
* Or we can stagger 5 contracts in a single trade. Add 1 contract every day

Here are the results

**(a)** _1 Contract Every Day (Max 5 Positions) > 45 DTE Expiry_

![images/2025/01/10/1736507558-1.png](/images/2025/01/10/1736507558-1.png)

![images/2025/01/10/1736507558-2.png](/images/2025/01/10/1736507558-2.png)

**(b)** _Ladder positions over time. Add 1x every day until we have 5 contracts on a single expiry._

![images/2025/01/10/1736507558-3.png](/images/2025/01/10/1736507558-3.png)

![images/2025/01/10/1736507558-4.png](/images/2025/01/10/1736507558-4.png)

**(c)** _Use all 5 contract at once on a single trade._

![images/2025/01/10/1736507558-5.png](/images/2025/01/10/1736507558-5.png)

![images/2025/01/10/1736507558-6.png](/images/2025/01/10/1736507558-6.png)

**(a)** looks better in terms of expectancy ratio and drawdowns.
Even though the overall returns are much better with **(c)**

### Complete table

![images/2025/01/10/1736507558-7.png](/images/2025/01/10/1736507558-7.png)

**(a)** => Blue

**(b)** => Orange

**(c)** => Green

![images/2025/01/10/1736507558-8.png](/images/2025/01/10/1736507558-8.png)

  

