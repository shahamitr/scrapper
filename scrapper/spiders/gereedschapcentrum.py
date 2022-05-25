import scrapy
import csv
import pkgutil
import time
from random import randint
import os

directory = os.getcwd()
filepath = directory+"/resources/gyzs_ean.csv"

#filepath = (os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'resources', 'gyzs_ean.csv')))
filepath = ('resources/gyzs_ean.csv')

csv_file = pkgutil.get_data("scrapper", "resources/gyzs_ean.csv") #csv inladen
# csv_file = pkgutil.get_data("bouwsales", "resources/link_bouwsales.csv")
csv_reader = csv.reader(csv_file.decode('utf-8').splitlines(), delimiter=',')


#open file
#file = open(filepath)
    
#read file
#csv_reader = csv.reader(file)

#store header of file
header = []
header = next(csv_reader)
header


#store ean from file

list_ean = []

for line in csv_reader:
    list_ean.append(line)
list_ean = str(list_ean)
list_ean = list_ean.replace("[", "")
list_ean = list_ean.replace("]", "")
list_ean = list_ean.replace("'", "")
list_ean = list_ean.replace(" ", "")
list_ean = list_ean.split(",")

class GereedschapcentrumSpider(scrapy.Spider):
    name = 'gereedschapcentrum'
    allowed_domains = ['gereedschapcentrum.nl']
    start_urls = ['http://gereedschapcentrum.nl/']

    name = 'Gereedschapcentrum'
    allowed_domains = 'gereedschapcentrum.nl'
    start_urls = ['https://www.gereedschapcentrum.nl/catalogsearch/result/?q={}'.format(list_ean[i]) for i in range(len(list_ean))]

    def parse(self, response,):
        time.sleep(randint(1, 2))
        data = {}
        prijs_eu = str(response.xpath('//*[@id="maincontent"]/div[4]/div[1]/div/div[2]/ol/li/div/div[2]/div[2]/span[2]/span/span[2]/span/text()').getall())
        prijs_eu = prijs_eu.replace(",", ".")
        prijs_eu = prijs_eu.replace("[", "")
        prijs_eu = prijs_eu.replace("]", "")
        prijs_eu = prijs_eu.replace("'", "")
        prijs_cent = str(response.xpath('//*[@id="maincontent"]/div[4]/div[1]/div/div[2]/ol/li/div/div[2]/div[2]/span[2]/span/span[2]/span/sup/text()').getall())
        prijs_cent = prijs_cent.replace("[", "")
        prijs_cent = prijs_cent.replace("]", "")
        prijs_cent = prijs_cent.replace("'", "")
        prijs = prijs_eu + prijs_cent
        if prijs != '':
            ean = str(response.xpath('//*[@id="search"]/@value').getall())
            ean = ean.replace("[", "")
            ean = ean.replace("]", "")
            ean = ean.replace("'", "")
            titel = str(response.xpath('//*[@id="maincontent"]/div[4]/div[1]/div/div[2]/ol/li/div/div[2]/strong/a/text()').getall())
            titel = titel.replace(']', '')
            titel = titel.replace('[', '')
            titel = titel.replace("'", "")
            data['Ean'] = ean
            data['Gereedschapcentrum'] = prijs
            data['Gereedschapcentrum-Titel'] = titel
            yield data
