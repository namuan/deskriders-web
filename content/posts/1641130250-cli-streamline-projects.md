+++
date = 2022-01-02T13:32:35
title = "Keeping multiple projects consistent"
description = ""
slug = ""
tags = []
externalLink = ""
series = []
+++
        
Here is a command I run to compare and streamline multiple projects.

It is run from a project which is already up to date and it requires having `diffmerge` available in your PATH.

```shell
TARGET_DIR="../tele-muninn"; echo '.pre-commit-config.yaml
Makefile
init-new-project.sh
init-template.sh
.flake8
setup.cfg
.github/actions/python-poetry-env/action.yml
.github/workflows/build.yml
.github/workflows/dependencies.yml
.github/workflows/publish.yml
pyproject.toml' | while read file; do echo "Comparing: $file"; test -f "$TARGET_DIR/$file" || cp $file "$TARGET_DIR/$file"; diffmerge "$file" "$TARGET_DIR/$file"; done; cd $TARGET_DIR
```

Once it finishes, you'll end up in the target folder which changes can be manually reviewed and committed.