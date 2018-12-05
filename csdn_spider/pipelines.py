# -*- coding: utf-8 -*-
# comment: 下载图片以及保存文章到sqlite数据库

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from factorys import csdn_article_table
import re
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
from csdn_spider.items import ArticleItem, ImageItem

from os.path import splitext
from urllib.parse import urlparse


class CsdnSpiderPipeline(object):
    def process_item(self, item, spider):
        return item


class CsdnArticlePipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, ArticleItem):
            if csdn_article_table.is_exists(item["id"], item["time"]) == False:
                csdn_article_table.insert({
                    "id": item['id'],
                    "title": item['title'],
                    "author": item['author'],
                    "time": item['time'],
                    "read_count": item['read_count'],
                    "tags": item['tags'],
                    "content": item['content']
                })
        return item


class ImagesrenamePipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        if isinstance(item, ImageItem):
            # meta里面的数据是从spider获取，然后通过meta传递给下面方法：file_path
            yield Request(item["url"], meta={"article_id": item["article_id"], "index": item["index"]})

    # 重命名，若不重写这函数，图片名为哈希，就是一串乱七八糟的名字
    def file_path(self, request, response=None, info=None):
        # todo: get response header to decide img extension
        # 获取图片后缀名,如果没有,默认为jpeg
        parse_url = urlparse(request.url)
        # path = urlparse(request.url).path
        ext = splitext(parse_url.path)[1]
        if ext == "":
            parse_url.path += ".jpeg"
            # image_name = parse_url.scheme +"://"+parse_url
            # ext = "jpeg"
        image_name = parse_url.scheme + "://" + parse_url.netloc + parse_url.path
        image_name = image_name.replace("/", "_")
        # 过滤windows字符串，不经过这么一个步骤，你会发现有乱码或无法下载
        image_name = re.sub(r'[？\\*|“<>:/]', '', image_name)
        filename = u'{0}/{1}'.format(request.meta["article_id"], image_name)
        return filename
