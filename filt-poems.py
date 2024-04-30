import json
import re

with open('poems-origin.json', 'r') as file:
    poems = json.load(file)

for p in poems:
    content = poems[p].strip()

    # author
    first_line = content.split('\n', 1)[0]
    if len(first_line) < 10:
        author = first_line
        content = content.split('\n', 1)[1]
    else:
        author = ""

    # lines
    lines = re.split(r'，|。|？|！|：|；|‘|’|“|”|\n', content)
    lines = [line for line in lines if line]

    poems[p] = {
        'title': p.strip('《》'),
        'author': author,
        'content': lines
    }


json.dump(poems, open('poems.json', 'w', encoding='utf-8'))
