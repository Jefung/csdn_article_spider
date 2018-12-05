# -*- coding: utf-8 -*-
import scrapy
from csdn_spider.items import ArticleItem,ImageItem
import re


class CsdnSpider(scrapy.Spider):
    name = 'csdn'
    # allowed_domains = ['https://blog.csdn.net/']
    keyword = "区块链"

    # start_urls = ['https://so.csdn.net/so/search/s.do?p=1&q=%E5%8C%BA%E5%9D%97%E9%93%BE&t=blog']

    def start_requests(self):
        url = "https://so.csdn.net/so/search/s.do?q={keyword}&t={type}&p=".format(keyword="区块链", type="blog")
        for i in range(1, 1001):
            new_url = url + str(i)
            yield scrapy.Request(new_url, callback=self.parse_blog_id)

    def parse_blog_id(self, response):
        # 获取文章id
        article_urls = response.css(".search-list-con .link a::attr(href)").extract()
        for article_url in article_urls:
            # pattern = "https://blog.csdn.net/jwter87/article/details/53423634"
            id = re.findall(r"article\/details\/(\d+)", article_url)[0]
            yield scrapy.Request(article_url, meta={"id": id}, callback=self.parse_blog_article)

    def parse_blog_article(self, response):
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)
        # 匹配文章内容
        item = ArticleItem()
        item['id'] = response.meta["id"]
        # item['content'] = "".join(response.css("#content_views *::text").extract())
        item["content"] = "\n".join(response.css("#content_views *::text,#content_views img").extract())
        item['title'] = response.css(".title-article::text").extract_first()
        item['time'] = response.css(".article-info-box .time::text").extract_first()
        item['author'] = response.css(".article-info-box .follow-nickName::text").extract_first()
        item['read_count'] = response.css(".article-info-box .read-count::text").re(r"阅读数：(\d+)")[0]
        item['tags'] = ''.join(response.css(".article-info-box .tags-box.artic-tag-box a::text").re("(.*?)[\t]+"))
        yield item

        # 处理文章图片
        img_urls = response.css(".article_content img::attr(src)").extract()
        for url in img_urls:
            img_item = ImageItem()
            img_item["article_id"] = item["id"]
            img_item["url"] = url
            img_item["index"] = img_urls.index(url)
            yield img_item

        # 匹配文章下方的推荐博客链接(ps: 有些是推荐下载, 推荐关键词, 不匹配)
        pattern = 'href="(https://blog.csdn.net/.*?/article/details/\d+)".*?title="(.*?)"'
        ls = response.css(".recommend-item-box.type_blog>div>a").re(pattern)
        if len(ls) % 2 != 0:
            return
        else:
            for i in range(0, len(ls)):
                if i % 2 != 0 and ls[i].find(self.keyword) != -1:
                    # pattern = "https://blog.csdn.net/jwter87/article/details/53423634"
                    id = re.findall(r"article\/details\/(\d+)", ls[i-1])[0]
                    yield scrapy.Request(ls[i-1], meta={"id": id},callback=self.parse_blog_article)
