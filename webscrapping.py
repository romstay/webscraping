import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.worldometers.info/coronavirus/country/india/')

after_bs = BeautifulSoup(page.content,   'html.parser')

find_data = after_bs.find(id="maincounter-wrap")

for x in find_data:
    print(x.text)