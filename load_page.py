""" Loading the webpage """

import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.fincaraiz.com.co/apartamentos/arriendo/medellin/')
content = page.content

soup = BeautifulSoup(content, 'html.parser')
print(soup.prettify())
