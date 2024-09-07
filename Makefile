export PROJECTNAME=$(shell basename "$(PWD)")
export IMAGE_FILE=$(shell date +%s).png

.SILENT: ;               # no need for @

setup-macos: ## Install dependencies etc
	echo "Installing dependencies"
	brew install hugo
	brew install netlify-cli

process: ## Here is the process
	echo "Write blog entry in vNote. Make sure to use the correct filename"
	echo "Copy Path from vNote"
	echo "Run /bin-utils/publish_vnote_to_hugo.py"
	echo "make serve -- to check it locally"
	echo "make deploy -- to push it live"
	echo "make commit-all -- to commit the changes"

clean: ## Clean Docs folder
	rm -rf docs

generate: clean opt-images ## Generator Documentation
	HUGO_ENV="production" hugo --gc --destination docs || exit 1

opt-images: ## Optimise images
	python3 image_optimizer.py --path static/images -v

commit-all: opt-images ## Push generated documentation to Github
	git add -A
	git commit -m "Updated docs"
	git push origin master

serve: opt-images ## Serve site locally
	open http://localhost:1313
	hugo server -D --disableFastRender

new: ## Hugo command to create a new entry
	echo "Write blog entry in vNote. Make sure to use the correct filename"
	echo "Copy Path from vNote"
	echo "Run /bin-utils/publish_vnote_to_hugo.py"
	echo "OR hugo new (posts|notes|projects)/next-title.md"

new-post: ## Create a new post with the given title (Use this with title=blah blah)
	hugo new posts/`date +%s`-$(title).md

paste-image: ## Paste image from clipboard and return markdown link
	mkdir -vp static/images/`date +%Y`/`date +%m`/`date +%d`
	echo "`pwd`/static/images/`date +%Y`/`date +%m`/`date +%d`/${IMAGE_FILE}" | pbcopy
	echo "Copy following markdown snippet and paste it in the post"
	echo "![image](/images/`date +%Y`/`date +%m`/`date +%d`/${IMAGE_FILE})"
	echo "Paste the image in the document. IntelliJ should save it as img.png"
	echo "mv content/posts/img.png static/images/`date +%Y`/`date +%m`/`date +%d`/${IMAGE_FILE}"
	echo "Or if you have file path then copy the path of source image and run the following command"
	echo "mv source-path static/images/`date +%Y`/`date +%m`/`date +%d`/${IMAGE_FILE}"

deploy: generate ## Deploys to Netlify staging environment
	netlify deploy --prod --dir=docs

deploy-push: deploy commit-all ## Deploys and then commits changes to Github
	echo "✅ All Done!"

.PHONY: help
.DEFAULT_GOAL := help

help: Makefile
	echo
	echo " Choose a command run in "$(PROJECTNAME)":"
	echo
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
	echo