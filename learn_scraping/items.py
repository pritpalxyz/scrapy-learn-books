# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LearnScrapingItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    rating = scrapy.Field()
    image_url = scrapy.Field()
    product_description = scrapy.Field()
    upc = scrapy.Field()
    direct_url = scrapy.Field()
    no_of_reviews = scrapy.Field()
