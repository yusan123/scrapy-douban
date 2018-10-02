# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem


class DoubanSpiderSpider(scrapy.Spider):
    # 爬虫的名字，不能和项目名重复
    name = 'douban_spider'
    # 允许的域名 不在该域名下的内容不会被爬取
    allowed_domains = ['movie.douban.com']
    # 开始的url
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        movie_list = response.xpath("//div[@class='article']//ol[@class='grid_view']/li")
        for item in movie_list:
            movie_item = DoubanItem()
            movie_item["number"] = item.xpath(".//div[@class='item']//em/text()").extract_first()
            movie_item["name"] = item.xpath(".//div[@class='hd']//span[@class='title'][1]/text()").extract_first()
            content = item.xpath(".//div[@class='info']//div[@class='bd']/p[1]/text()").extract()
            for i_content in content:
                content_s = "".join(i_content.split())
                movie_item["introduce"] = content_s
            movie_item["star"] = item.xpath(".//div[@class='info']//div[@class='star']/span[2]/text()").extract_first()
            movie_item["evaluate"] = item.xpath(
                ".//div[@class='info']//div[@class='star']/span[last()]/text()").extract_first()
            movie_item["describe"] = item.xpath(".//div[@class='info']//p[@class='quote']/span/text()").extract_first()
            # print(movie_item)
            yield movie_item
        next_link = response.xpath("//span[@class='next']/link/@href").extract()
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request("https://movie.douban.com/top250" + next_link, callback=self.parse)
