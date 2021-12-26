+++
date = 2021-12-19T12:23:12
title = "Using helium - a Selenium API wrapper"
description = "A quick example of using Helium as a Selenium API wrapper to automate browser interactions."
slug = ""
tags = ["python", "selenium"]
externalLink = ""
series = []
+++
        
Here is a quick example to use [Helium](https://github.com/mherrmann/selenium-python-helium).

![Helium](/images/2021/12/516002003606105.gif)
### Steps:

1. Install dependencies using pip or add it to `requirements.txt` and run `pip3 install -r requirements.txt`
```shell
pip3 install helium
# or
pip3 install -r requirements.txt
```

2. Create a python file and paste the following code.

```python3
#!/usr/bin/env python3
"""
Demonstrates how to use helium to automate a web browser.
"""
from helium import start_firefox

def main():
    driver = start_firefox()
    driver.execute_script("window.alert('Hello World')")


if __name__ == "__main__":
    main()
```

Here I'm using `Firefox` but it is easy to switch to `Chrome`.

### References:

[Github](https://github.com/mherrmann/selenium-python-helium) |
[Documentation](https://selenium-python-helium.readthedocs.io/en/latest/) |
⭐⭐⭐ [Cheat sheet](https://github.com/mherrmann/selenium-python-helium/blob/master/docs/cheatsheet.md)
