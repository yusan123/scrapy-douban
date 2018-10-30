# -*- coding: utf-8 -*-
import scrapy
from meitu.items import MeituItem
from urllib import parse
from scrapy.http import Request
class MeizituSpider(scrapy.Spider):
    name = 'meizitu'
    allowed_domains = ['www.rtz.cc']
    start_urls = ['https://www.rtz.cc/html/xiee/']

    def parse(self,response):
        url_list = response.xpath("//ul[@class='detail-list']//li/a/@href").extract()
        for url in url_list:
            yield scrapy.Request(parse.urljoin(response.url,url),callback=self.parse_item)
        next_page = response.xpath("//div[@class='page-show']//a[last()]/@href").extract_first()
        if next_page:
            yield scrapy.Request(parse.urljoin(response.url,next_page),callback=self.parse)

    def parse_item(self, response):
        item = MeituItem()
        item['pics'] = response.xpath("//div[@class='pp hh']//a//img/@src").extract()
        item['title'] = response.xpath("//div[@class='des']//h1/text()").extract_first()
        yield item
        next_page = response.xpath("//div[@class='page-show']//a[last()]/@href").extract_first()
        if next_page:
            yield scrapy.Request(parse.urljoin(response.url,next_page),callback=self.parse_item)
