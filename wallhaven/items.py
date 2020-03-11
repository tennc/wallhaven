# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WallhavenItem(scrapy.Item):
    # define the fields for your item here like:
    imgpageurl = scrapy.Field()
    imageurl = scrapy.Field()
    imagesize = scrapy.Field()
    #pass
