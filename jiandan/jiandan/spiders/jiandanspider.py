# -*- coding: utf-8 -*-
import scrapy
from jiandan.items import JiandanItem


class JiandanspiderSpider(scrapy.Spider):
    name = 'jiandanspider'
    allowed_domains = ['www.meituri.com']
    start_urls = ['https://www.meituri.com/zhongguo/']

    def parse(self, response):

        itemList = response.xpath("//div[@class='hezi']//li")
        # print(item["image_urls"])

        for i in itemList:
            item = JiandanItem()
            item["pic0urls"] = i.xpath("./a/img/@src").extract_first()
            item["title"] = i.xpath(".//p[@class='biaoti']//text()").extract_first()
            item["picNum"] = i.xpath(".//span[@class='shuliang']//text()").extract_first()
            item["modelName"] = i.xpath(".//p[2]/a//text()").extract_first()
            item["organization"] = i.xpath(".//p[1]/a//text()").extract_first()
            tagList = i.xpath(".//p[3]//a//text()").extract()
            item["tags"] = "-".join(tagList)
            print(item)
            yield item
        next_url = response.xpath("//div[@id='pages']//a[last()]/@href").extract()
        if next_url:
            next_url = next_url[0]
            yield scrapy.Request("https://www.meituri.com" + next_url, callback=self.parse)
