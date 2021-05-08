# program to find top stories from google news

import bs4
from bs4 import BeautifulSoup as soup
import requests

news_url = "https://news.google.com/news/rss"

client = requests.get(news_url).content

soup_page = soup(client, "xml")

news_page = soup_page.findAll("item")

for news in news_page:
    print(news.title.text)
    print(news.link.text)
    print(news.pubDate.text)
    print("~" * 70)
