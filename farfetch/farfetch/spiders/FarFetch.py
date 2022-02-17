import scrapy

from ..items import FarfetchItem


class FarFetch(scrapy.Spider):
    name="farfetch"
    # start_urls=['https://www.farfetch.com/fr/shopping/men/shoes-2/items.aspx']
    start_urls = [
        'http://quotes.toscrape.com/tag/humor/',
    ]

    # def parse(self, response):
    #     items = FarfetchItem()
    #     print(response)
    #     # name =response.xpath('//p[@data-component="ProductCardBrandName" and @itemprop="brand"]').get()
    #     pass
    #     # yield name
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'author': quote.xpath('span/small/text()').get(),
                'text': quote.css('span.text::text').get(),
            }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)