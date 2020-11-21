# This is the smaller example of web scrapping
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# To ignore ssl certificstes error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input("enter the url: ")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
# retrive ancher tags
tags = soup("a")
for tag in tags:
    print(tag.get("href", None))
