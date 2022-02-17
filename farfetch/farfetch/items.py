# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FarfetchItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    brand = scrapy.Field()
    original_price=scrapy.Field()
    sale_price = scrapy.Field()
    image_url = scrapy.Field()
    product_page_url = scrapy.Field()
    product_category = scrapy.Field()




# - `name` [store as string]
# - `brand` [store as string]
# - `original_price` [store as float]
# - `sale_price` [store as float] : if the website is showing just one price for a product. You can keep this same as the original_price.
# - `image_url` [store as string]
# - `product_page_url` [store as string]
# - `product_category` [store as string] [ it can contain 2 values "Footwear" or "Bags and Purses" ]