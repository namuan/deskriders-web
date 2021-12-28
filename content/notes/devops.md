---
title: "DevOps"
date: 2021-12-19T15:46:00Z
---

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



### Notes
