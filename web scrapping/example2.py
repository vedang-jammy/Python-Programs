import requests
import bs4

result = requests.get('https://en.wikipedia.org/wiki/Elon_Musk')

soup = bs4.BeautifulSoup(result.text, 'lxml')

for item in soup.select('.toctext'):
    print(item.text)
    
musk = soup.select('.thumbimage')[1]

print(musk['src'])

img_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/SpaceX_CEO_Elon_Musk_visits_N%26NC_and_AFSPC_%28190416-F-ZZ999-006%29_%28cropped%29.jpg/170px-SpaceX_CEO_Elon_Musk_visits_N%26NC_and_AFSPC_%28190416-F-ZZ999-006%29_%28cropped%29.jpg')

f = open('musk.jpg','wb')  #used to download image to your computer using python
f.write(img_link.content)
f.close()