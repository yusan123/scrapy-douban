# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import pymysql
from douban.settings import *


class DoubanPipeline(object):
    # def __init__(self):
    #     self.client = pymysql.connect(
    #         host=MYSQL_HOST,
    #         port=MYSQL_PORT,
    #         user=MYSQL_USER,
    #         passwd=MYSQL_PASSWD,
    #         db=MYSQL_DBNAME,
    #         charset=MYSQL_CHARSET
    #     )
    #     self.cur = self.client.cursor()

    def process_item(self, item, spider):
        sql = "insert into douban250 values(%s,%s,%s,%s,%s,%s)"
        data = (item["number"], item["name"], item["introduce"], item["star"], item["evaluate"], item["describe"])
        self.cur.execute(sql, data)
        self.client.commit()
        return item
