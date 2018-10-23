# -*- coding: utf-8 -*-
import scrapy
from bole.items import BoleItem
from scrapy.http import Request
from urllib import parse
#//div[@class='post floated-thumb']//div[1]/a/@href  可以拿到所有文章的每个文章的连接
class ArticlespiderSpider(scrapy.Spider):
    name = 'articleSpider'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        post_nodes = response.xpath("//div[@class='post floated-thumb']//div[1]/a")
        for node in post_nodes:
            pic_url = node.xpath("./img/@src").extract_first()
            url = node.xpath("./@href").extract_first()
            yield Request(parse.urljoin(response.url,url),meta={"pic_url":pic_url},callback=self.parse_detail)
        nexturl = response.xpath("//a[@class='next page-numbers']/@href").extract_first()
        if nexturl:
            yield Request(nexturl,callback=self.parse)

    def parse_detail(self, response):
        item = BoleItem()
        item['pic_url'] = [response.meta.get("pic_url","")]
        item['title']=response.xpath("//div[@class='entry-header']/h1/text()").extract_first()
        item['time'] = response.xpath("//div[@class='entry-meta']/p/text()").extract()[0].replace("·","").strip()
        item['tag'] = response.xpath("//div[@class='entry-meta']/p/a[last()]/text()").extract_first()
        item['source'] = response.xpath("//div[@class='copyright-area']/a/@href").extract_first()
#        item['content'] = response.xpath("//div[@class='entry']").extract_first()
        print(item)
        yield item
