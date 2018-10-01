# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    number = scrapy.Field() #电影编号
    name = scrapy.Field() #电影名称
    introduce = scrapy.Field() #电影简介
    star = scrapy.Field() #电影评分
    evaluate = scrapy.Field() #电影评论数
    describe = scrapy.Field() #电影描述


