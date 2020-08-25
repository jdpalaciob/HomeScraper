""" Script to filter the data by tags on the HTML code """

# from bs4 import BeautifulSoup
from load_page import page_request

URL = 'https://www.fincaraiz.com.co/apartamentos/arriendo/medellin/'
html_ = page_request(URL)

property_grid = html_.find_all('ul', {'itemtype':'http://schema.org/Product'})
# print(property_grid[0])
property_location_tag = property_grid[0].find('h2', {'class':'h2-grid'})
property_location = property_location_tag.text.strip()
# print(property_location)

locations =[]
areas = []
hab = []
for prop in property_grid:
    property_location_tag = prop.find('h2', {'class':'h2-grid'})
    property_location = property_location_tag.text.strip()
    locations.append(property_location)

    characteristics_tag = prop.find('li', {'class':'surface li_advert'})
    property_characteristics = characteristics_tag.text.strip().replace(' ','').replace('\n','').replace('\r','').replace('m2',' ').replace('hab.', '')
    characteristics = property_characteristics.split(sep=' ')
    property_area = characteristics[0]
    property_hab = characteristics[1]
    areas.append(property_area)
    hab.append(property_hab)
print(hab)