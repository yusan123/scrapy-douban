# -*- coding: utf-8 -*-
import scrapy
from jiandan.items import JiandanItem
from urllib import parse

class JiandanspiderSpider(scrapy.Spider):
    name = 'jiandanspider'
    allowed_domains = ['www.27270.com']
    start_urls = ['http://www.27270.com/ent/rentiyishu/2017/172906.html']

    # def start_requests(self):
    #     reqs = []
    #     url = 'http://www.mmjpg.com/mm/1499'
    #     req = scrapy.Request(url,callback=self.parse,dont_filter=True)
    #     reqs.append(req)
    #     return reqs
    def parse(self, response):
        pic_urls = response.xpath("//div[@class='articleV4Body']/p/a[1]/img/@src").extract()
        item = JiandanItem()
        item['pics'] = pic_urls
        yield item
        next_url = response.xpath("//div[@class='page-tag oh']//li[@id='nl']/a/@href").extract_first()
        if next_url:
            yield scrapy.Request(parse.urljoin(response.url,next_url), callback=self.parse)
