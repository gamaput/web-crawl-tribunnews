import scrapy
from scrapy.selector import Selector
# from kompas.items import KompasItem

class ItemNews(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    # images = scrapy.Field()
    category = scrapy.Field()
    date = scrapy.Field()
    desc = scrapy.Field()

class KompasSpider(scrapy.Spider):
    name = "kompas"
    allowed_domains = ["kompas.com"]
    start_urls = [
        # "http://indeks.kompas.com",
        'https://indeks.kompas.com/?site=tekno&date=2022-10-5'
    ]

    def parse(self, response):
        """ This function parses a property page.

        @url http://indeks.kompas.com
        @returns items
        """

        indeks = Selector(response).xpath('//div[@class="article__list clearfix"]')

        for indek in indeks:
            item = ItemNews()
            item['title'] = indek.xpath('div[@class="article__list__title"]/h3/a/text()').extract_first()
            item['link'] = indek.xpath('div[@class="article__list__title"]/h3/a/@href').extract_first()
            #item['images'] = indek.xpath('div[@class="article__list__asset clearfix"]/div/img/@src').extract_first()
            item['category'] = indek.xpath('div[@class="article__list__info"]/div[@class="article__subtitle article__subtitle--inline"]/text()').extract_first()
            item['date'] = indek.xpath('div[@class="article__list__info"]/div[@class="article__date"]/text()').extract_first()
            item['desc'] = ""

            yield item