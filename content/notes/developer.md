---
title: "Development Apps/Tools/Tips and Tricks"
date: 2021-12-19T15:46:00Z
---

### Apps

* HTTP Toolkit -> https://httptoolkit.tech/
Intercept & view all your HTTP(S) Mock endpoints or entire servers Rewrite, redirect, or inject errors
Open source -> https://github.com/httptoolkit

**QuickDraw**

Found [quickdraw](https://github.com/maxchuquimia/quickdraw) which is an app for drawing over the screen.
Unfortunately, it doesn't seem to provide any packages, and I'm unable to build it locally.
A similar application which is quite good is [Pensela](https://github.com/weiameili/Pensela).

![](/images/2021/12/pensela.png)

### Command Line Tools

* ImageMagick Resize a bunch of images using ImageMagick

```shell
find ./static -name '*.png' | while read line; do convert -resize 1280x1280 $line $line; done
```

* Combine and convert list of images into a single PDF

```shell
convert IMG_00{09..18}.JPG IMG_0025.JPG IMG_00{19..20}.JPG IMG_0026.JPG IMG_00{21..24}.JPG Final-Doc.pdf
```

* jq: Length of array

```shell
$ echo '["123", "567", "abc"]' | jq '. | length'
```

* Shell: Pass contents of clipboard as file descriptor. It'll work with apps expecting file argument.

```shell
$ command <(pbpaste)
```

* Convert: Resize image

```shell
$ convert -quality 75% -resize 40x40 twitter.png twitter-icn.png
```
* Ctrl X-E to quickly edit current command

{{< youtube Uin5cYqY7y8 >}}

* [Comby](https://comby.dev/docs/get-started) examples

[Refactor request API](https://comby.live/index.html#%7B%22source%22:%22request.config('./base.json')%5Cnrequest.get('https://api.com/users')%5Cnrequest.post('https://api.com/users')%5Cn%22,%22match%22:%22request.:%5Bmethod%5D(:%5Barg1%5D)%22,%22rule%22:%22where%20:%5Bmethod%5D%20!=%20%5C%22config%5C%22%22,%22rewrite%22:%22request(%7B%20url:%20:%5Barg1%5D,%20method:%20':%5Bmethod%5D'%20%7D)%22,%22language%22:%22.generic%22,%22substitution_kind%22:%22in_place%22,%22id%22:0%7D)

### Homebrew

__Updating packages___
```shell
brew update
```

__Cleaning up brew__
```shell
brew bundle dump # Writes all installed casks/formulae/taps to Brewfile
brew bundle --force cleanup # Removes all dependencies not listed in Brewfile
```

### Hugo

__Build with drafts__
```shell
hugo -D serve
```

### Sqlite

[Sqlite](https://sqlite.org/index.html)

[Sql.js](https://github.com/sql-js/sql.js)

[sql.js-httpvfs](https://github.com/phiresky/sql.js-httpvfs)

_Here are few links for future reference_

https://phiresky.github.io/blog/2021/hosting-sqlite-databases-on-github-pages/

https://github.com/segfall/static-wiki

https://github.com/ilmalte/github-actions-with-sqlite

https://github.com/phiresky/sql.js-httpvfs/issues/22

* Sqlite JSON Support: https://dgl.cx/2020/06/sqlite-json-support

* Sqlite DB Migration with PRAGMA user_version: https://levlaz.org/sqlite-db-migrations-with-pragma-user_version/

* Auto generate GraphQL server -> https://github.com/bradleyboy/tuql

* Undo/Redo with SQLite -> https://www.sqlite.org/undoredo.html

* Verneuil: streaming replication for sqlite -> https://github.com/backtrace-labs/verneuil


### PostgreSQL

* Postgres is a great pub/sub & job server https://webapp.io/blog/postgres-is-the-answer/

* Turning PostgreSQL into a queue serving 10,000 jobs per second https://gist.github.com/chanks/7585810

* PostgREST Starter Kit: https://github.com/subzerocloud/postgrest-starter-kit

### Database Notes

* Membership schema -> https://github.com/membership/membership.db

### Jenkins

https://github.com/hoto/jenkinsfile-examples
> Executable examples of Jenkinsfiles.

https://github.com/oleg-nenashev/demo-jenkins-config-as-code
> Demo of Jenkins Configuration-As-Code with Docker and Groovy Hook Scripts

https://gitlab.com/stavros/harbormaster
> Harbormaster is a small utility that lets you easily deploy multiple Docker-Compose applications on a single host.

https://dockerswarm.rocks/

* Hello CloudRun -> https://codelabs.developers.google.com/codelabs/cloud-run-hello-python3?hl=en#0

* Jenkins As Code -> https://fishi.devtail.io/weblog/2019/01/12/jenkins-as-code-part-2/

* Ansible Best Practices -> https://max.engineer/six-ansible-practices

* Jenkins wrangling -> https://coderanger.net/jenkins/

### Security

* OpenSSH Security -> https://linux-audit.com/audit-and-harden-your-ssh-configuration/

* Automated security testing -> https://devops.com/automated-security-testing-continuous-delivery-pipeline/

* GitSecrets -> https://git-secret.io/ , Another alternative to GitCrypt -> https://www.agwa.name/projects/git-crypt/

### Docker

* Inspecting Docker traffic -> https://skynet.sexy/2015/05/inspect-docker-traffix-on-osx

* Docker container to capture all host traffic -> https://jerrygamblin.com/2016/05/28/a-docker-container-to-capture-all-traffic-from-host/

* TcpDump in Docker -> https://husobee.github.io/http/tcpdump/docker/2016/11/30/troubleshooting-http-docker-tcpdump.html

* Run more stuff in Docker -> https://jonathan.bergknoff.com/journal/run-more-stuff-in-docker/
```shell
alias aws='docker run --rm -v ~/.aws:/.aws -v "$(pwd)":"$(pwd)" -w "$(pwd)" -u 1000:1000 -e AWS_PROFILE mikesir87/aws-cli:1.18.11 aws'
alias jq='docker run -i --rm jess/jq jq'
```

Hugo
```shell
hugo = docker run --rm -u $$(id -u):$$(id -g) -v "$$(pwd)":/src -v "$$(pwd)"/output:/target $(2) klakegg/hugo:0.54.0-ext-alpine $(1)

hugo-watch:
    mkdir -p output
    $(call hugo, server, -it -p 1313:1313)
```

Python
```shell
run_container = docker run -i --rm -u $$(id -u):$$(id -g) -v "$$(pwd)":"$$(pwd)" -w "$$(pwd)" $(3) $(1) $(2)
python = $(call run_container, python:3.8.2-alpine3.11, $(1), -e PYTHONUSERBASE="$$(pwd)"/vendor $(2))

dependencies:
    $(call python, pip install --user -r requirements.txt, -e XDG_CACHE_HOME=$(user_cache_dir) -v "$(user_cache_dir)":"$(user_cache_dir)")

repl:
    $(call python, python)

run:
    $(call python, python -m app.main)

# where user_cache_dir is set elsewhere to ~/.cache on Linux or ~/Library/Caches on a Mac.
```

### AWS

* On-Demand test environments -> https://mherman.org/blog/on-demand-test-environments-with-docker-and-aws-ecs/

* AWS Tips -> https://wblinks.com/notes/aws-tips-i-wish-id-known-before-i-started/
  And -> https://launchbylunch.com/posts/2014/Jan/29/aws-tips/

* Push files to s3 with Github actions -> https://til.simonwillison.net/github-actions/s3-bucket-github-actions

### GoLang

* Go: Qt Binding https://github.com/therecipe/qt

### Java

* Testing framework built on Cucumber JVM -> https://sukesh15.gitbooks.io/cucumber-jvm-test-framework-/content/

* Investigating thread dumps -> http://www.captaindebug.com/2012/10/investigating-deadlocks-part-3.html

* Statemachines -> https://github.com/davidmoten/state-machine/blob/master/README.md

* Microservices -> https://www.slideshare.net/danveloper/microservices-the-right-way

### Java Notes

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

### Python

* Puppeteer -> https://pypuppeteer.readthedocs.io/en/latest/

* Devices -> https://github.com/puppeteer/puppeteer/blob/v1.18.1/lib/DeviceDescriptors.js

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

#### Flask

https://github.com/damian-ontivero/servertree
> Made with Python (Flask), HTML, CSS3, JavaScript (A little) and SQLAlchemy as ORM.

* Building Flask Apps: https://hackersandslackers.com/series/build-flask-apps/

* Generator -> https://github.com/ksh7/flask-starter

#### PyQt

* Useful widgets for PyQt5 -> https://github.com/kadir014/pyqt5-custom-widgets

* Some useful apps based on PyQt5. ->https://github.com/taseikyo/PyQt5-Apps

* System tray & Mac menu bar applications -> https://www.pythonguis.com/tutorials/system-tray-mac-menu-bar-applications-pyqt/

* Iconic fonts in PyQt and PySide applications -> https://github.com/spyder-ide/qtawesome

#### Graphics / Diagrams

https://github.com/p5py/p5
>  p5 is a Python package based on the core ideas of Processing.

* Yed examples with Python -> https://github.com/bockor/pyyed-real-life-examples

* Python dependency graph using yed (generates GraphML) -> https://github.com/vijeshm/pythondependencygraph

* Network analysis in Python -> https://github.com/networkx/networkx

#### Machine Learning

* https://github.com/tom-doerr/fix
  Suggests solutions for errors in the command line. It is using OpenAI's Codex AI to come up with suggestions.

#### Gaming

https://github.com/CharlesPikachu/Games
>  Games: Create interesting games by pure python.

https://github.com/tasdikrahman/spaceShooter
>  🎮 The classic retro game recreated using Pygame and python

https://github.com/jatinmandav/Gaming-in-Python
>  Code to all the Games made using Python Programming Language

* FlappyBird -> https://pygamezero-bird.readthedocs.io/en/latest/part1.html

### Testing Tools

[webium](https://github.com/wgnet/webium)

> Webium is a Page Object pattern implementation library for Python (http://martinfowler.com/bliki/PageObject.html). It allows you to extend WebElement class to your custom controls like Link, Button and group them as pages.

* Api Documentation -> https://github.com/Redocly/redoc

* Generating millions of HTTP requests -> https://dak1n1.com/blog/14-http-load-generate/

### Other Useful websites

* Minimal Pastebin -> https://github.com/wantguns/bin

* Turns your Python functions into microservices with web API, interactive GUI -> https://github.com/ml-tooling/opyrator

* Edit and regenerate plots and graphs -> https://pylustrator.readthedocs.io/en/latest/
