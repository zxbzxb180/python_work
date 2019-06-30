# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EastmoneyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    number = scrapy.Field()
    name = scrapy.Field()
    latest_price = scrapy.Field()
    amount_of_rise_and_fall = scrapy.Field()
    rate_of_rise_and_fall = scrapy.Field()
    today_opening_price = scrapy.Field()
    maximum_price = scrapy.Field()
    minimum_price = scrapy.Field()
    yesterday_closing_price = scrapy.Field()
    amplitude = scrapy.Field()
    update_time = scrapy.Field()