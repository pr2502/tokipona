#!/bin/python3

import jinja2, json

def file_to_json(fname):
    with open(fname) as f:
        return json.load(f)


words = file_to_json("wordlist.json")
kinds = file_to_json("kinds.json")

with open("template.html") as f:
    template = jinja2.Template(f.read())

print(template.render(words = words, kinds = kinds))
