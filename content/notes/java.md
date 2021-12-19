---
title: "Java/JVM"
date: 2021-12-19T15:46:00Z
---

### Notes

* Java: URLEncoder does form encoding instead of percent encoding - https://stackoverflow.com/questions/4737841/urlencoder-not-able-to-translate-space-character

* Java: Initialise a CharArray from a String

```java
private String reservedCharacter = "!#$%&'()*+,/:;=?@[]";
private char[] chars = reservedCharacter.toCharArray();
```

* Java/JUnit5 : Parameterized testing with JUnit 5

```java
@ParameterizedTest(name = "{0} should be \"{1}\"")
    @CsvSource({
            "http://www.example.com, http%3A%2F%2Fwww.example.com",
            "?query=123, %3Fquery%3D123"
    })
    public void testPercentEncodeAsciiString(String source, String expected) {
        // when
        String result = PercentEncoding.encode(source);

        // then
        assertEquals(expected, result);
    }
```

* Java: Generating a mvn wrapper

```java
$ mvn -N io.takari:maven:0.7.7:wrapper
```

