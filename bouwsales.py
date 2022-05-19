import scrapy


class BouwsalesSpider(scrapy.Spider):
    name = 'bouwsalesnl'
    allowed_domains = ['bouwsales.nl']
    start_urls = ['http://bouwsales.nl/']

    def parse(self, response):
        pass
