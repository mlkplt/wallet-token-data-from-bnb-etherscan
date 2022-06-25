from eth_keys import keys
import requests
from bs4 import BeautifulSoup

def value(url):
    html = requests.get(url, headers={'User-agent': 'Chrome/94.0.4606.61'}).text
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("ul", {"class": "list list-unstyled mb-0"}).text.split('\n')
    value=table[1]
    return value
