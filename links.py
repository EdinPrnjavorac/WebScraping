import requests
from bs4 import BeautifulSoup


html = requests.get(
    'https://www.msn.com/en-us/money/stockdetails/').text
bs = BeautifulSoup(html, "lxml")
possible_links = bs.find_all('a')
for link in possible_links:
    if link.has_attr('href'):
            print(link.attrs['href'])
