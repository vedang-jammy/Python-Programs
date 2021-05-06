import requests
import re
import os.path
from os import path
import bs4
from bs4 import BeautifulSoup
from datetime import datetime

def getcontents():
    url = 'https://www.mohfw.gov.in/'
    r = requests.get(url)
    txt = " "
    if r.status_code == 200:
        txt = r.text
        return txt


def scrape_now():
    total_list = []
    state_list = []
    confirmed_list = []
    recovered_list = []
    death_list = []
    
    txt = getcontents()
    soup = BeautifulSoup(txt , 'html.parser')
    
    total = soup.find('div', {'class':'site-status-count'})
    for length in total.find_all('strong'):
        total_list.append(length.getText())
    
    state_data = soup.find("section", {"id": "state-data"})
    tables = state_data.find_all('tbody')
    for row in tables[0].findAll("tr"):
        col = row.findAll("td")
        if((col[0].getText()).isnumeric()):
            state_list.append(col[1].getText())
            confirmed_list.append(int(col[2].getText()))
            recovered_list.append(int(col[3].getText()))
            death_list.append(int(col[4].getText()))
    return total_list, state_list, confirmed_list, recovered_list, death_list
