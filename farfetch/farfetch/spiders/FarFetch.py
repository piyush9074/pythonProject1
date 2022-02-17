import scrapy

from ..items import FarfetchItem


class FarFetch(scrapy.Spider):
    name="farfetch"
    start_urls=['https://www.farfetch.com/fr/shopping/men/shoes-2/items.aspx']


    def parse(self, response):
        items = FarfetchItem()
        main = response.xpath("//ul[@data-testid='product-card-list']/div")


        for i in range(main):

            brand =main.xpath('//p[@data-component="ProductCardBrandName" and @itemprop="brand"]//text()').extract()[i]
            name =main.xpath('//p[@data-component="ProductCardDescription" and @itemprop="name"]//text()').extract()[i]
            price = main.xpath('//div[@data-component="PriceBrief" and @itemprop="offers"]//p[@data-component="Price"]//text()').extract()[i]
            image_url = main.xpath('//div[@data-component="ProductCardImageContainer"]//img[@data-component="ProductCardImagePrimary"]/@src').extract()[i]
            link = main.xpath('//div[@data-component="ProductCard" and @itemprop="itemListElement"]//a[@data-component="ProductCardLink"]/@href').extract()[i]
            items['brand']=brand
            items['name'] = name
            items['original_price'] = price
            items['product_page_url'] = link

            yield items