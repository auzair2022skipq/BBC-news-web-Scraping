import requests
import json
from bs4 import BeautifulSoup

url = 'https://www.bbc.com/news'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

articles = []
for article in soup.find_all('div', class_='gs-c-promo-body gel-1/2@xs gel-1/1@m gs-u-mt@m'):
    title = article.find(class_="gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text").text.strip()
    print(title)
    summary = article.find('p',class_="gs-c-promo-summary gel-long-primer gs-u-mt nw-c-promo-summary")
    
    link = article.find('a', class_='gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor')['href']
    articles.append({'title':title,'link':link})

with open('bbc_news.json', 'w') as f:
    json.dump(articles, f)
print(articles)
print(summary)