import json
import requests
from bs4 import BeautifulSoup as bs


res = requests.get("https://www.unifesp.br/campus/sjc/corpodocente.html")
res.encoding = "utf-8"
soup = bs(res.text, 'html.parser')
posts = soup.find_all(class_='table table-hover')


all_post = []
for post in posts:
    info = post.find(class_='post-content')
    title = info.h2.a.text
    preview = info.p.text
    date = info.footer.time['datetime']
    img = post.find(class_='wp-post-image')['src']
    author = post.find(class_='post-author').text
    all_post.append({
        'title': title,
        'preview': preview,
        'date': date,
        'author': author[5:],
        'img': img
    })

with open('posts.json', 'w') as json_file:
    json.dump(all_post, json_file, indent=3, ensure_ascii=False)
