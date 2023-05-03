'''
Hi, This script will scrape news from Times of India website and will give links and titles of some trending news in India.
Made with Python
Good luck
'''
import requests
from bs4 import BeautifulSoup

url = "https://timesofindia.indiatimes.com/india"


response = requests.get(url)
soup = BeautifulSoup(response.content,'html.parser')
news = soup.find('div', {'id':'c_0301'})
source = news.find_all('span',{'class':'w_tle'})

title = []
links = []


for i in source:
    t = i.find('a')['title']
    title.append(t)
    l = i.find('a')['href']
    links.append(l)

for i in range(len(links)):
    print("Title: ", title[i])
    print('Link: https://timesofindia.indiatimes.com'+links[i])
    print()