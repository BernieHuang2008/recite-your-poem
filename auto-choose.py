import json
import random

poems = json.load(open('poems.json', 'r', encoding='utf-8'))
poems = list(poems.values())

while 1:
    index = random.randint(0, len(poems) - 1)
    poem = poems[index]
    print(f"《{poem['title']}》（{poem['author']}）")
    print(random.choice(poem['content']))
    print('\n'*6)
    if input():
        print(f"《{poem['title']}》（{poem['author']}）")
        print("\n".join(poem['content']))
        input()
