""" Creating an object containing the webpage html code """

import requests
from bs4 import BeautifulSoup

def page_request(url):
    """ Creates an object with the HTML code """
    page = requests.get(url).content

    return BeautifulSoup(page, 'html.parser')

if __name__ == '__main__':

    URL = 'https://www.fincaraiz.com.co/apartamentos/arriendo/medellin/'
    print(page_request(URL))
