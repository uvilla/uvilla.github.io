.PHONY: pubs check serve build clean help

help:
	@echo "make pubs    regenerate _data/publications.yml from files/uvilla.bib"
	@echo "make check   parse the .bib and report problems, writing nothing"
	@echo "make serve   build and serve locally at http://127.0.0.1:4000"
	@echo "make build   build the site into _site/"

pubs:
	python3 scripts/bib2yaml.py

check:
	python3 scripts/bib2yaml.py --check

serve: pubs
	bundle exec jekyll serve --livereload

build: pubs
	bundle exec jekyll build

clean:
	rm -rf _site .jekyll-cache
