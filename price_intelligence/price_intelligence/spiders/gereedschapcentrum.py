import scrapy


class GereedschapcentrumSpider(scrapy.Spider):
    name = 'gereedschapcentrum'
    allowed_domains = ['gereedschapcentrum.nl']
    start_urls = ['http://gereedschapcentrum.nl/']

    def parse(self, response):
        pass
