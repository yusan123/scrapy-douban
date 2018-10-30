# -*- coding: utf-8 -*-
import scrapy
from shengse.items import ShengseItem
from urllib import parse


class ShengseSpiderSpider(scrapy.Spider):
    name = 'shengse_spider'
    allowed_domains = ['ygdppt.com']
    start_urls = ['http://mp333.ygdppt.com/365/2017/lyx/bfml/%E5%86%B0%E5%B3%B0%E9%AD%94%E6%88%8001.mp3']



    def parse(self, response):
        for i in range(1,92):
            item = ShengseItem()
            item['file_url'] = ['http://mp333.ygdppt.com/365/2017/lyx/bfml/%E5%86%B0%E5%B3%B0%E9%AD%94%E6%88%80'+'%02d.mp3' % i]
            yield item


