# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
from jiandan.settings import *
import os
from scrapy.http import Request

class MyImagePipeline(ImagesPipeline):
    #暂时还不清楚为什么要这样写，不能使用父类的这个方法，直接调用父类这个方法也不行======但是为什么只能用item传递
    # 父类方法如下
    # def get_media_requests(self, item, info):
    #     return [Request(x) for x in item.get(self.images_urls_field, [])]


    def get_media_requests(self, item, info):
        request_objs = super().get_media_requests(item, info)  #调用父类方法后，返回一个Request对象的列表
        for request_obj in request_objs:
            #原来是这个意思，在这里给每个Request，添加item属性，
            # request传递到下边方法时file_path,就能从request中取出item,再取出title
            #因为下边的方法中拿不到item，就通过request传递了item
            request_obj.item = item   #按说只是传值过去 #request_obj.title = item['title']就不行，明明下边request方法中又title这个属性
        return request_objs

    def file_path(self, request, response=None, info=None):
        # 这个方法是在图片将要被存储的时候调用，来获取这个图片存储的路径
        path = super().file_path(request,response,info)
       # category = request.get('title')  #拿到item中的目录名,是在
        category = request.item['title']  #拿到item中的目录名,是在
        store_path = os.path.join(IMAGES_STORE,category)  #使用os.path,将配置的图片保存路径和新建的目录拼接起来
        #不存在新的目录，则创建，存在的话，就不会再创建了，这样同一组的图片就放到同一个目录下了
        if not os.path.exists(store_path):
            os.makedirs(store_path)
        #从父类自带的file_path中提取出处理过的文件名
        image_name = os.path.split(path)[1]
        #文件名和之前的目录再拼接起来，组成最终图片的保存路径
        file_path = os.path.join(store_path,image_name)
        return file_path


