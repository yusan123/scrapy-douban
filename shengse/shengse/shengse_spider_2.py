# -*- coding: utf-8 -*-
import scrapy
from shengse.items import ShengseItem
from urllib import parse



class ShengseSpiderSpider(scrapy.Spider):
    name = 'shengse_spider'
    allowed_domains = ['yee022.com']
    start_urls = ['https://www.yee022.com/mp3list/6-insert_time-1.html']

    def parse(self, response):
        item_urls = response.xpath("//div[@class='item']//ul[@class='clearfix']//li//a/@href").extract()
        for item_url in item_urls:
            yield scrapy.Request(parse.urljoin(response.url,item_url), callback=self.parse_detail)
        next_page = response.xpath("//div[@class='hy-page clearfix']//li[last()-1]/a/@href").extract_first()
        if next_page:
            yield scrapy.Request(parse.urljoin(response.url, next_page), callback=self.parse)

    def parse_detail(self, response):
        item = ShengseItem()
        item['file_url'] = response.xpath("//audio/@src").extract()
        yield item
