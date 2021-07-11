#!/bin/python3

#
# Parse Toki Pona wordlist from <http://tokipona.net/tp/ClassicWordList.aspx>
# into json
#
# The output schema looks like this:
#
# {
#   "$word": {
#       "img": "$path_to_glyph_image",
#       "data": {
#           "dt": "$title_with_symbols" | null,
#           "dd": [
#               {
#                   "kind": "$part_of_speech" | null,
#                   "desc": "$english_description",
#               }
#               ...
#           ],
#       },
#   },
#   ...
# }
#
# Usage:
# $ wget -O wordlist.html "http://tokipona.net/tp/ClassicWordList.aspx"
# $ ./scrape.py < wordlist.html > wordlist.json
#

import sys, bs4, json


def map_dd(dd):
    return {
        "kind": None if dd.i is None else dd.i.string,
        "desc": list(dd.stripped_strings)[-1],
    }


def map_table(table):
    data = table.find("dl")

    if data is None: return None

    img = table.find("img")
    name = data.a["name"]

    return (name, {
        "img": img["src"], 
        "data": {
            "dt": data.dt.string,
            "dd": list(map(map_dd, data.find_all("dd", lang="en"))),
        },
    })


inp = sys.stdin.read()
soup = bs4.BeautifulSoup(inp, "html.parser")
tables = soup.find_all("table")

print(json.dumps(
    dict(
        filter(lambda x: x is not None,
            map(map_table, tables)))))
