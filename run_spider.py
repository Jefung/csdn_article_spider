# comment: 爬虫启动文件
from scrapy import cmdline

if __name__ == '__main__':
    cmdline.execute("scrapy crawl csdn".split())
