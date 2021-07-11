tp.html: template.html generate.py wordlist.json kinds.json
	./generate.py < $< > $@

wordlist.json: ClassicWordList.aspx.htm scrape.py
	./scrape.py < $< > $@

watch:
	find . | entr make tp.html

.PHONY: watch
