# -*- coding: utf-8 -*-
import scrapy
from jiandan.items import JiandanItem
from urllib import parse

class JiandanspiderSpider(scrapy.Spider):
    name = 'jiandanspider'
    allowed_domains = ['www.27270.com']
    start_urls = ['http://www.27270.com/ent/meinvtupian/']

#需要公共的变量列表来保存一组图的url


    def parse(self, response):
        nodes = response.xpath("//div[@class='MeinvTuPianBox']//li")
        #每一个节点就是一个图集
        for node in nodes:
            url = node.xpath("./a/@href").extract_first()
            title = node.xpath("./a[1]/@title").extract_first()
            yield scrapy.Request(parse.urljoin(response.url,url),meta={"title":title},callback=self.parse_detail)

        #翻页加载更多图片列表
        next_page = response.xpath("//div[@class='NewPages']//li[13]/a/@href").extract_first()
        if next_page:
            yield scrapy.Request(parse.urljoin(response.url,next_page),callback=self.parse)


    #解析每一张图片的url,通过分页
    def parse_detail(self, response):
        title = response.meta.get('title')
        item = JiandanItem()
        item['pic'] = response.xpath("//div[@class='articleV4Body']/p/a[1]/img/@src").extract()
        item['title'] = title
        yield item
        next_pic_url = response.xpath("//div[@class='page-tag oh']//li[@id='nl']/a/@href").extract_first()
        if next_pic_url:
            yield scrapy.Request(parse.urljoin(response.url,next_pic_url),meta={"title":title},callback=self.parse_detail)




