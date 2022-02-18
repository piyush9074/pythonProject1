import scrapy

from ..items import FarfetchItem


class FarFetch(scrapy.Spider):
    name="farfetch1"
    start_urls=['https://www.farfetch.com/fr/shopping/men/shoes-2/items.aspx']


    def parse(self, response):
        items = FarfetchItem()
        main = response.xpath("//ul[@data-testid='product-card-list']/div/a")
        # for i in range(96):
        #     image_url = main.xpath('//div[@data-component="ProductCardImageContainer"]//img[@data-component="ProductCardImagePrimary"]/@src').extract()[i]
        #     items['image_url']=image_url
        #     yield items

        next_page =response.xpath('//a[@data-testid="page-next"]').extract_first()
        np = response.css("a[data-testid='page-next']::attr(href)").extract()

        items['name']=next_page
        yield items
