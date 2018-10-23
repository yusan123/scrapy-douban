# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from bole.settings import *
import pymysql
from scrapy.pipelines.images import ImagesPipeline

class BolePipeline(object):
    def __init__(self):
        self.client = pymysql.connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            passwd=MYSQL_PASSWD,
            db=MYSQL_DB,
            charset=MYSQL_CHARSET
        )
        self.cur = self.client.cursor()

    def process_item(self, item, spider):
        sql = "insert into jobbole values(%s,%s,%s,%s,%s)"
        data = (item['title'], item['time'], item['tag'], item['source'], item['content'])
        self.client.ping()  #加上这个语句，可以防止mysql 自动断开
        self.cur.execute(sql, data)
        self.client.commit()
        return item
class BoleImagePipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        for ok,value in results:
             item['pic_path'] = value['path']
        return item