# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BoleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #标题
    title = scrapy.Field()
    #时间
    time = scrapy.Field()
    #标签分类
    tag = scrapy.Field()
    #文章正文
    content = scrapy.Field()
    #原文链接
    source = scrapy.Field()
    #文章的第一个张图片
    pic_url = scrapy.Field()
    #下载图片本地存储的路径
    pic_path = scrapy.Field()

    pass
