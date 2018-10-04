# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import requests

class JiandanPipeline(object):
    def process_item(self, item, spider):
        dir_path ='E:/%s'%spider.name
        print(dir_path)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        for img_url in item['image_urls']:
            list_name = img_url.split("/")
            file_name = list_name[-1]
            file_path="%s/%s"%(dir_path,file_name)
            if os.path.exists(file_name):
                continue
            with open(file_path,'wb') as file_writer:
                # conn = (img_url)#下载图片
                file_writer.write(requests.get(img_url).content)
            file_writer.close()
        return item