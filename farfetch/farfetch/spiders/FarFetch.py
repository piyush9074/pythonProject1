import scrapy

from ..items import FarfetchItem


class FarFetch(scrapy.Spider):
    name="farfetch"
    # start_urls=['https://www.farfetch.com/fr/shopping/men/shoes-2/items.aspx']
    start_urls=['https://www.farfetch.com/fr/shopping/women/bags-purses-1/items.aspx','https://www.farfetch.com/fr/shopping/men/shoes-2/items.aspx']
    pg_number=2

    def parse(self, response):
        items = FarfetchItem()
        main = response.xpath("//ul[@data-testid='product-card-list']/div/a")
        current_url = response.url
        count=0
        for i in main:

            brand =i.xpath('//p[@data-component="ProductCardBrandName" and @itemprop="brand"]//text()').extract()[count]
            name =i.xpath('//p[@data-component="ProductCardDescription" and @itemprop="name"]//text()').extract()[count]
            price = i.xpath('//div[@data-component="PriceBrief" and @itemprop="offers"]//p[@data-component="Price"]//text()').extract()[count]
            # image_url = i.xpath('//div[@data-component="ProductCardImageContainer"]//img[@data-component="ProductCardImagePrimary"]/@src').extract()[count]
            image_url = main.xpath('//div[@data-component="ProductCardImageContainer"]//img[@data-component="ProductCardImagePrimary"]/@src').extract()[count]
            link = i.xpath('//div[@data-component="ProductCard" and @itemprop="itemListElement"]//a[@data-component="ProductCardLink"]/@href').extract()[count]
            # price=str(price)
            price = price.encode("ascii", "ignore")
            price=float(price.decode().strip())
            product_category="Footwear"
            if "women" in link:
                product_category="Bags and Purses"

            items['brand']=str(brand)
            items['name'] = str(name)
            items['original_price'] = price
            items['sale_price']=price
            items['product_page_url'] = "farfetch.com"+link
            items['image_url']=image_url
            items['product_category']=product_category
            count=count+1
            yield items

        #autoLink fetch error chk xpath
        # next_page = response.xpath('//div/a[@data-testid="page-next"]/@href').extract()
        # print(next_page)


        url=f"https://www.farfetch.com/fr/shopping/men/shoes-2/items.aspx?page={FarFetch.pg_number}&view=90&sort=3&scale=282"
        # pg_str="https://www.farfetch.com/fr/shopping/men/shoes-2/items.aspx"
        if (FarFetch.pg_number < 203):
            FarFetch.pg_number +=  1
            yield response.follow(url, callback=self.parse)
