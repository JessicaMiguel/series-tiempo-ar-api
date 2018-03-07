SHELL = bash

.PHONY: docs servedocs doctoc

docs:
	mkdocs build
	$(BROWSER) site/index.html

servedocs:
	mkdocs serve

doctoc: ## generate table of contents, doctoc command line tool required
        ## https://github.com/thlorenz/doctoc
	doctoc --github --title " " docs/api_reference.md
	bash fix_github_links.sh docs/api_reference.md
	doctoc --github --title " " docs/quick_start.md
	bash fix_github_links.sh docs/quick_start.md
	doctoc --github --title " " docs/spreadsheet_integration.md
	bash fix_github_links.sh docs/spreadsheet_integration.md

swaggerdocs:
	wget https://github.com/swagger-api/swagger-ui/archive/master.zip -O temp.zip; unzip -jo temp.zip 'swagger-ui-master/dist/*' -d docs/swagger; rm temp.zip
	sed -i "s/url: \".*\"/url: \"\.\.\/series-tiempo-api-ar\.swagger\.yml\"/g" docs/swagger/index.html

serveswaggerdocs:
	echo "Browse to http://localhost:8000/docs/swagger/"
	python -m SimpleHTTPServer 8000	
