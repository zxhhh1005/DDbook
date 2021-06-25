# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DDBOOKItem(scrapy.Item):
    # define the fields for your item here like:
    b_name = scrapy.Field()
    b_info = scrapy.Field()
    b_pic = scrapy.Field()
    w_name = scrapy.Field()
    p_name = scrapy.Field()
    p_time = scrapy.Field()
    s_price = scrapy.Field()
    pre_price = scrapy.Field()
    disc = scrapy.Field()
    url = scrapy.Field()
    ISBN = scrapy.Field()
