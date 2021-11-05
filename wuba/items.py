# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WubaItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    gongci = scrapy.Field()
    yueli = scrapy.Field()
    new_url = scrapy.Field()

