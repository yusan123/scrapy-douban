# -*- coding: utf-8 -*-
import scrapy
from jiandan.items import JiandanItem

class JiandanspiderSpider(scrapy.Spider):
    name = 'jiandanspider'
    allowed_domains = ['http://www.mmjpg.com']
    start_urls = ['http://www.mmjpg.com/mm/1005']

    def parse(self, response):
        item = JiandanItem()
        item["image_urls"] = response.xpath("//div[@class='content']//img//@src").extract()
        #print(item["image_urls"])
        yield  item
        next_url = "http://www.mmjpg.com"+ response.xpath("//div[@class='page']//a[@class='ch next']//@href").extract_first();
        print(next_url)
        if next_url:
            yield scrapy.Request(next_url,callback=self.parse)
