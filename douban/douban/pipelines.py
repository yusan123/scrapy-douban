# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class DoubanPipeline(object):


    def __init__(self):
        self.client=pymysql.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            passwd="123",
            db="scrapy",
            charset="utf8"
        )
        self.cur= self.client.cursor()

    def process_item(self, item, spider):
        sql = "insert into douban250 values(%s,%s,%s,%s,%s,%s)"
        data=(item["number"],item["name"],item["introduce"],item["star"],item["evaluate"],item["describe"]);
        self.cur.execute(sql,data)
        self.client.commit()
        return item
