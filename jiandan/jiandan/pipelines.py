# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import requests
import pymysql
from jiandan.settings import *


class JiandanPipeline(object):
    def __init__(self):
        self.client = pymysql.connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            db=MYSQL_DBNAME,
            user=MYSQL_USER,
            passwd=MYSQL_PASSWD,
            charset=MYSQL_CHARSET
        )
        self.cur = self.client.cursor()

    def process_item(self, item, spider):
        sql = "insert into meituri_zhongguo values(%s,%s,%s,%s,%s,%s)"
        data =(item["organization"],item["modelName"],item["picNum"],item["tags"],item["title"],item["pic0urls"])
        self.cur.execute(sql,data)
        self.client.commit()
        return item
