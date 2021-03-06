# -*- coding: utf-8 -*-
# comment: 数据结构item, 用于组件间传递通信


# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy



class ArticleItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    time = scrapy.Field()
    author = scrapy.Field()
    read_count = scrapy.Field()
    tags = scrapy.Field()
    content = scrapy.Field()

class ImageItem(scrapy.Item):
    article_id = scrapy.Field()
    url = scrapy.Field()
    index = scrapy.Field()
    # name = scrapy.Field()

