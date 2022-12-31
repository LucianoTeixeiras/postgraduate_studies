import scrapy


class ImdbRatingSpider(scrapy.Spider):
    name = 'imdb_rating'
    allowed_domains = ['www.imdb.com']
    start_urls = ['http://www.imdb.com/']

    def parse(self, response):
        pass
