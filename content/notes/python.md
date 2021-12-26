---
title: "Python"
date: 2021-12-19T15:46:00Z
---

### Flask

https://github.com/damian-ontivero/servertree
> Made with Python (Flask), HTML, CSS3, JavaScript (A little) and SQLAlchemy as ORM.

* Building Flask Apps: https://hackersandslackers.com/series/build-flask-apps/


### PyQt

https://github.com/kadir014/pyqt5-custom-widgets
>  More useful widgets for PyQt5

https://github.com/taseikyo/PyQt5-Apps
> Some useful apps based on PyQt5.

https://www.pythonguis.com/tutorials/system-tray-mac-menu-bar-applications-pyqt/
> System tray & Mac menu bar applications

### Graphics

https://github.com/p5py/p5
>  p5 is a Python package based on the core ideas of Processing.

### Gaming

https://github.com/CharlesPikachu/Games
>  Games: Create interesting games by pure python.
 
https://github.com/tasdikrahman/spaceShooter
>  🎮 The classic retro game recreated using Pygame and python

https://github.com/jatinmandav/Gaming-in-Python
>  Code to all the Games made using Python Programming Language

* FlappyBird -> https://pygamezero-bird.readthedocs.io/en/latest/part1.html

### Notes

* Python: How to get a class name from a type

```python
class A:
	pass

a = A()
print(a.__class__.__name__)

# or
print(type(a).__name__)
```

* Python: List sub directories

```python
tool_codegen_dir: Path = Path(__file__)
print([x.name for x in tool_codegen_dir.iterdir() if x.is_dir()])
```

* Python/PyQt: One way to handle focusOut event by installing event filter on the widget

```py
# Installing event filter
self.parent.txt_scratch_pad.installEventFilter(self.events)

# where self.events in a class with a QObject parent class - like ScratchPadEvents 👇

# Then override eventFilter method in that class
class ScratchPadEvents(QObject):
    def __init__(self, parent, app):
        super().__init__(parent)

    def eventFilter(self, source: QObject, event: QEvent):
        if event.type() == QtCore.QEvent.FocusOut:
            # do something
            pass

        return super().eventFilter(source, event)
```

* Python/PyQt5: TextEdit Widget Scroll to top

```python
def scroll_to_top(txt_edit_widget):
    txt_cursor: QTextCursor = txt_edit_widget.textCursor()
    txt_cursor.movePosition(QTextCursor.Start)
    txt_edit_widget.setTextCursor(txt_cursor)
```

* Python/PyQt5: Replacing Text in a PlainTextEdit without losing undo/redo history

```python
def replace_text(self, txt_edit_widget, new_text):
    txt_cursor: QTextCursor = txt_edit_widget.textCursor()
    txt_cursor.select(QTextCursor.Document)
    txt_cursor.insertText(new_text)
```

* Python/JsonPath: Filtering JSON using JsonPath.

```python
pip install jsonpath-ng

from jsonpath_ng.ext import parse as jsonpath_parse

def filter_json_path(self, json_doc, path_query):
    if not json_doc:
        return

    parsed_query = jsonpath_parse(path_query)
    key_found = parsed_query.find(json_doc)
    if key_found:
        return key_found[0].value
    else:
        return None
```

* Python : Python one liner to extract and transform Spring HttpStatus enums Raw

```python
curl -s https://raw.githubusercontent.com/spring-projects/spring-framework/master/spring-web/src/main/java/org/springframework/http/HttpStatus.java | \
grep '\".*),' | \
while read line; \
  do echo $line | python -c 'import re,sys; s, c, m = re.search("([\w\_]+)\((\d+),\s+\"([\w\s]+)", sys.stdin.readline()).groups(); print("{}: (\"HttpStatus.{}\", \"{}\"),".format(c, s, m))'; \
done
```

* Python: Find words in a sentence

```python
source = 'The quick brown fox jumps over the lazy dog'

import re
print(re.findall(r'\b(\w+)\b', source))
```

* Python/Jinja: Using Jinja template in a simple Python script

```shell
$ cat template.j2
{{ description }}
```

```python
# pip install Jinja2

from jinja2 import Environment, FileSystemLoader

TEMPLATE_DIR = os.path.dirname(os.path.abspath(__file__))

jinja_env = Environment(loader=FileSystemLoader(TEMPLATE_DIR), trim_blocks=True)

book_item = dict(
	description="Hello World"
)

rendered = jinja_env.get_template("template.j2").render(book_item)
print(rendered)
```

* Python: A Quick script to collect data from website

```python
from pathlib import Path
import re
import subprocess
import time

def run_command(command):
  return subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True).decode('utf-8')
  
link_rgx = re.compile("Link\s=\s\"(.*)\"")

def process_file(file):
  text = file.read_text()
  link = link_rgx.findall(text)[0]
  cmd = "curl -s " + link + ' | pup \'div.stacked div.left a.actionLinkLite text{}\' | head -n 1'
  category = run_command(cmd)
  category = category.strip()
  print("Running {}".format(cmd))
  print("Category Found for {} is {}".format(link, category))
  cmd = 'sed -i.bak \'s/categories = \[""\]/categories = \["' + category + '"\]/g\' ' + file.as_posix()
  print("Running {}".format(cmd))
  run_command(cmd)
  time.sleep(5)

def main():
  p = Path.cwd().joinpath("books")
  for f in p.iterdir():
    process_file(f)

if __name__=="__main__":
  main()
```

* Python/PyQt: Open file dialog box

```python
from PyQt5.QtWidgets import QFileDialog

def open_file(self, dialog_title, dialog_location, file_filter=None):
    return QFileDialog.getOpenFileName(
        self, dialog_title, dialog_location, filter=file_filter
)

file_location, _ = self.main_window.save_file(
    "Export Environments",
    current_project_folder,
    file_filter="Environment Files (*.envs.json)",
)

if file_location:
	# do something
	pass
```
