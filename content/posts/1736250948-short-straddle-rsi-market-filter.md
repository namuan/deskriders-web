+++ 
date = 2025-01-07T11:55:48Z
title = "Short Straddles with RSI based market filters"
description = "Show back tests on RSI based market filter strategy"
slug = ""
tags = ["options", "trading", "data analysis", "backtesting"]
categories = ["Trading", "Data Analysis", "Python"]
externalLink = ""
series = []
+++

Hypothesis: What if we avoid new trade if RSI is overbought or oversold?

Backtest with different RSI thresholds and different RSI periods

**RSI Thresholds:**

```text
RSI Period: 4

rsi_low_values=(0 10 20 30)  
rsi_high_values=(70 80 90 100)
```

![images/2025/01/07/1736255462-1.png](/images/2025/01/07/1736255462-1.png)

Best Parameters by Expectancy Ratio:

1. **rsi_low_threshold=20, rsi_high_threshold=100**  
   Expectancy Ratio: 1.08  
   This combination shows the highest expectancy ratio, indicating it provides the best risk-adjusted returns.
2. rsi_low_threshold=30, rsi_high_threshold=100  
   Expectancy Ratio: 1.06  
   Second-best expectancy ratio.
3. rsi_low_threshold=30, rsi_high_threshold=70  
   Expectancy Ratio: 1.04  
   Third-best expectancy ratio.

**Key Observations:**

* It is worth not trading when RSI is oversold. It could be due to further downside movement or potential strong pull back which can put the trade at a losing position at the start.
* The overbought indicator doesn't seem to have much impact.

Here is the breakdown by month

Note that these with 1 max position open at a time
![images/2025/01/07/1736255462-2.png](/images/2025/01/07/1736255462-2.png)

In comparison, here is the monthly breakdown if we take trade regardless of market condition (No RSI Filter)
![images/2025/01/07/1736255462-3.png](/images/2025/01/07/1736255462-3.png)

What if we compare 0-100, 30-100 with **5 max trades at once ?**

![images/2025/01/07/1736255462-4.png](/images/2025/01/07/1736255462-4.png)

Monthly breakdown with 5 trades at once:

![images/2025/01/07/1736255462-5.png](/images/2025/01/07/1736255462-5.png)

![images/2025/01/07/1736255462-6.png](/images/2025/01/07/1736255462-6.png)

**Observations:**

The drawdown during Covid period is better with the RSI 4 market filter but the always in strategy seems to perform better overall.

Testing it over a bunch of other RSI Periods

```text
RSI Period: 3 5 7 9 11 13

rsi_low_values=(0 30)  
rsi_high_values=(100)
```

![images/2025/01/07/1736255462-7.png](/images/2025/01/07/1736255462-7.png)

![images/2025/01/07/1736255462-8.png](/images/2025/01/07/1736255462-8.png)

In the end it does look like that keeping in trade all the trade is better than apply any RSI based filters.
It is more likely due to missing the trades which is going to recover any losses incurred.
