import scrapy
import csv
import time
from random import randint

#store ean from file

list_ean = [8713515012285,8713515012308,8713515013558,8713515012469,0088381662710,5025536634265,5025536359496,5025536333779,5025536529653,5025536631035]

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
        prijs_eu = str(response.xpath('//*[@id="maincontent"]/div[4]/div[1]/div/div[2]/ol/li/div').getall())
        prijs_eu = prijs_eu.replace(",", ".")
        prijs_eu = prijs_eu.replace("[", "")
        prijs_eu = prijs_eu.replace("]", "")
        prijs_eu = prijs_eu.replace("'", "")
        prijs_cent = str(response.xpath('//*[@id="maincontent"]/div[4]/div[1]/div/div[2]/ol/li/div/div').getall())
        prijs_cent = prijs_cent.replace("[", "")
        prijs_cent = prijs_cent.replace("]", "")
        prijs_cent = prijs_cent.replace("'", "")
        prijs = prijs_eu + prijs_cent
        if prijs != '':
            ean = str(response.xpath('//*[@id="search"]/@value').getall())
            ean = ean.replace("[", "")
            ean = ean.replace("]", "")
            ean = ean.replace("'", "")
            
            #title of the product
            titel = str(response.xpath('//*[@class="product-item-link"]/font/font').getall())
            titel = titel.replace(']', '')
            titel = titel.replace('[', '')
            titel = titel.replace("'", "")
            
            #link of the product
            link = str(response.xpath('//*[@class="product-item-link"]/@href').getall())
            link = link.replace(']', '')
            link = link.replace('[', '')
            link = link.replace("'", "")

            data['Ean'] = ean
            data['Gereedschapcentrum'] = prijs
            data['Gereedschapcentrum-Titel'] = titel
            data['Gereedschapcentrum-Link'] = link
            yield data
