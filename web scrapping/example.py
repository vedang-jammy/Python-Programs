import requests
import bs4
result = requests.get("http://www.example.com")
soup = bs4.BeautifulSoup(result.text, 'lxml')
print(soup.select('title'))
paragragraph = soup.select('p')
print(paragragraph[1])
print(paragragraph[1].getText())
