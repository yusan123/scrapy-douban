# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.files import FilesPipeline
from scrapy.http import Request
from shengse.settings import FILES_STORE
import os
class ShengsePipeline(object):
    def process_item(self, item, spider):
        return item

class MyFile(FilesPipeline):
    def get_media_requests(self, item, info):
        reqs = super().get_media_requests(item,info)
        for r in reqs:
            r.item = item
        return reqs

    def file_path(self, request, response=None, info=None):
        # item = request.meta['item']
        # novel_name = item['file_url'][0].split('/')[-1]
        # return '%s' % novel_name
        item = request.item
        novel_name = item['file_url'][0].split('/')[-1]
        path = os.path.join(FILES_STORE,novel_name)
        return path

    def item_completed(self, results, item, info):
        print(results)
        return item
