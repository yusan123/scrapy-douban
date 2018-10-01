# -*- coding: utf-8 -*-
import scrapy


class DoubanSpiderSpider(scrapy.Spider):
    #爬虫的名字，不能和项目名重复
    name = 'douban_spider'
    #允许的域名 不在该域名下的内容不会被爬取
    allowed_domains = ['movie.douban.com']
    #开始的url
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        print(response.text)
