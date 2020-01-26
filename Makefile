export PROJECTNAME=$(shell basename "$(PWD)")

.SILENT: ;               # no need for @

clean: ## Clean Docs folder
	rm -rf docs

generate: clean ## Generator Documentation
	HUGO_ENV="production" hugo --gc --destination docs || exit 1

commit-all: generate ## Push generated documentation to Github
	git add -A
	git commit -m "Updated docs"
	git push origin master

serve: ## Serve site locally
	open -a Firefox.app http://localhost:1313
	hugo server --disableFastRender

stage: generate ## Deploys to Netlify staging environment
	netlify deploy --dir=docs

.PHONY: help
.DEFAULT_GOAL := help

help: Makefile
	echo
	echo " Choose a command run in "$(PROJECTNAME)":"
	echo
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
	echo