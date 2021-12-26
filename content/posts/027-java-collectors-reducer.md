+++ 
date = 2020-04-19T13:05:38+01:00
title = "Java 8+: Using Collectors as reducers"
description = "In this simple example, we'll look at using Collectors to apply reduction to a list"
tags = ["java", "streams"]
externalLink = ""
series = []
+++

A simple example to show how to use Collectors as reducers in Java 8+.

Say, we have a simple `Transaction` class consists of the currency and the value of the transaction.

`Transaction` class is sprinkled with Lombok annotation to make use of Builder.

```java
    @Value
    @Builder
    public static class Transaction {
        String currency;
        int value;
    }
```

And given the following set of data:

__GBP Transactions = 2__, 
__USD Transactions = 1__,
__CAD Transactions = 1__

```java
    List<Grouping.Transaction> transactionList = List.of(
            Grouping.Transaction.builder().currency("GBP").value(1).build(),
            Grouping.Transaction.builder().currency("GBP").value(5).build(),
            Grouping.Transaction.builder().currency("USD").value(6).build(),
            Grouping.Transaction.builder().currency("CAD").value(9).build()
    );
```

We would like to group this list by transaction currency, so that

```java
    assertEquals(transactionsByCurrency.get("GBP").size(), 2);
    assertEquals(transactionsByCurrency.get("USD").size(), 1);
    assertEquals(transactionsByCurrency.get("CAD").size(), 1);
```

Here are the two approaches to implement this requirement.

```java
    public Map<String, List<Transaction>> imperative(List<Transaction> transactionList) {
        Map<String, List<Transaction>> transactionsByCurrency = new HashMap<>();

        for (Transaction transaction: transactionList) {
            List<Transaction> transactionForCurrency = transactionsByCurrency.computeIfAbsent(
                    transaction.getCurrency(), k -> new ArrayList<>()
            );

            transactionForCurrency.add(transaction);
        }

        return transactionsByCurrency;
    }
```

And let's compare that to using `Streams` and `Collectors` which ended up a lot less verbose and simple to understand.

```java
    public Map<String, List<Transaction>> functional(List<Transaction> transactionList) {
        return transactionList.stream()
                .collect(
                        Collectors.groupingBy(Transaction::getCurrency)
                );
    }
```
