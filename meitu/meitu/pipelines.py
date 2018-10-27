# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from meitu.settings import IMAGES_STORE
import os

class MeituPipeline(object):
    def process_item(self, item, spider):
        return item

class MyImage(ImagesPipeline):

    def get_media_requests(self, item, info):
        requests = super().get_media_requests(item,info)
        for request in requests:
            request.title = item['title']
        return requests

    def file_path(self, request, response=None, info=None):
        path = super().file_path(request,response,info)
        #item = request.get('item')
        dirname = request.title
        dir_path = os.path.join(IMAGES_STORE,dirname)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        filename = os.path.split(path)[1]
        file_path = os.path.join(dir_path,filename)
        return file_path

