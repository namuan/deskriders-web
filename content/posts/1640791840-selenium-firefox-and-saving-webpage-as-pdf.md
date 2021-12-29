+++
date = 2021-12-29T15:37:40
title = "Selenium Firefox and saving webpage as PDF"
description = ""
slug = ""
tags = []
externalLink = ""
series = []
+++
        
A quick sample to save a webpage as PDF using Selenium with Firefox. Here I'm using [Helium](https://github.com/mherrmann/selenium-python-helium) as a wrapper over Selenium but the same configuration can be directly applied to selenium library.

You can read more about using Helium [here](https://www.deskriders.dev/posts/1639863087-python-selenium/).

Installing the selenium wrapper

```shell
pip3 install helium
```

Python code

```python3
#!/usr/bin/env python3
from time import sleep

from helium import start_firefox
from selenium.webdriver import FirefoxOptions

options = FirefoxOptions()
options.add_argument("--start-maximized")
options.set_preference("print.always_print_silent", True)
options.set_preference("print.printer_Mozilla_Save_to_PDF.print_to_file", True)
options.set_preference("print_printer", "Mozilla Save to PDF")

driver = start_firefox("https://www.deskriders.dev/posts/1639863087-python-selenium/", options=options)

driver.execute_script("window.print();")
sleep(2)  # Found that a little wait is needed for the print to be rendered otherwise the file will be corrupted

driver.quit()

```

Once the above script is finished, you'll find `mozilla.pdf` in the current directly. 
