# 基于scrapy的CSDN文章爬虫

对所爬取数据的GUI界面展示: [Jefung/csdn_article_show](https://github.com/Jefung/csdn_article_show)

# 目录结构

* [csdn_spider](csdn_spider)
    * [spiders](csdn_spider\spiders)
        * [csdn.py](csdn_spider\spiders\csdn.py)&nbsp;:&nbsp; CSDN爬虫类<br/>
    * [items.py](csdn_spider\items.py)&nbsp;:&nbsp; 数据结构item, 用于组件间传递通信<br/>
    * [middlewares.py](csdn_spider\middlewares.py)
    * [pipelines.py](csdn_spider\pipelines.py)&nbsp;:&nbsp; 下载图片以及保存文章到sqlite数据库<br/>
    * [settings.py](csdn_spider\settings.py)&nbsp;:&nbsp; scrapy爬虫的自带配置文件<br/>
* [database](database)
    * [Spider](database\Spider)
       * [csdn_article.py](database\Spider\csdn_article.py)&nbsp;:&nbsp; 存储CSDN文章表的操作类<br/>
* [factorys](factorys)
    * [db_factory.py](factorys\db_factory.py)&nbsp;:&nbsp; 数据库工厂, 生产表实例<br/>
* [conf.py](conf.py)&nbsp;:&nbsp; 配置文件(数据库文件存放,图片目录)<br/>
* [README.md](README.md)
* [requirements.txt](requirements.txt)
* [run_spider.py](run_spider.py)&nbsp;:&nbsp; 爬虫启动文件<br/>
* [scrapy.cfg](scrapy.cfg)

---

## 如何运行
* 安装依赖: 在项目根目录下运行`pip install -r requirements.txt`
* 配置: 在配置文件 [conf.py](conf.py) 中配置数据库文件存放,图片目录,用于后续的
![6HX0IP2MD@UW448$6M[RJ99.png](http://images.jefung.cn/6HX0IP2MD@UW448$6M[RJ99.png)的使用
* 运行: `python run_spider.py`

## 爬虫思路
* 初始化url的选择:

既然是按照关键词爬取, 那就考虑在
[CSDN博客搜索页面](https://so.csdn.net/so/search/s.do?q=%E5%8C%BA%E5%9D%97%E9%93%BE&t=blog&o=&s=&l=)
下手

![1543991720(1).png](http://images.jefung.cn/1543991720(1).png)

研究后,我决定将从关键词搜索页(1-1000页)作为起始url.

* 怎么进一步爬取:

将起始url中的所有文章链接全部提取出来, 并进入文章爬取. CSDN的文章结构很清晰,参考
[10分钟弄懂当前各主流区块链架构 - 小牛BlOcK - CSDN博客](https://blog.csdn.net/weixin_42758350/article/details/81153647)
最上面是文章信息(作者/发布时间/阅读数/标签),中间是文章,最下面的推荐(推荐博客/广告/下载)

这里我是通过提取最下面的文章推荐来获取其它url,并通过文章标题的是否包含关键词来
过滤掉一些(因为推荐文章先是关键词相关的文章,然后还有很多乱七八糟的文章)

* 图片的处理

考虑到后续的处理, 文章中有图片, 所以图片还是得下载下来, 图片按照文章id来分目录,
一篇文章的所有图片在同一个目录下, 图片的命名我是直接对其url进行特殊处理并作为图片名

* 文章的处理

直接提取文章的所有内容(包含完整的图片标签img),并保存. 这里使用的是我自己对
python中最著名的ORM(Object Relationship Mapping)框架
[SQLAlchemy - The Database Toolkit for Python](https://www.sqlalchemy.org/)
的一个封装
[Jefung/SQLAlchemy_wrap: SQLAlchemy的封装,支持在指定文件夹中查找表对应类](https://github.com/Jefung/SQLAlchemy_wrap)

## 学习路线:
1. 先看[Scrapy1.5中文文档_Scrapy1.5中文文档_Scrapy 中文网](http://www.scrapyd.cn/doc/)
,学会怎么基本使用`scrapy`
2. 理解`scrapy`架构[Scrapy的架构 - 简书](https://www.jianshu.com/p/335ce3435a2b),这个最重要
3. 继续其它实战(见最下面链接)
4. 开始学习调试技巧, 调试技巧最重要, 开发时等出现问题来调试就很麻烦, 可以边开发
边使用`scrapy shell`来调试/判断提取数据是否正确. 由于我是使用`Pycharm`,
所以顺带看了下`scrapy`配合ide的调试方法.
5. 强烈推荐 [Toggle JavaScript - Chrome 网上应用店](https://chrome.google.com/webstore/detail/toggle-javascript/cidlcjdalomndpeagkjpnefhljffbnlo)
,一键禁止`Ajax`加载, 开发时对网页源码研究时最好开启,因为你爬虫爬的时候是不会自动`ajax`请求,
会造成你在浏览器控制台看到的html和爬虫爬的html不一样

## 参考链接
* [Scrapy1.5中文文档_Scrapy1.5中文文档_Scrapy 中文网](http://www.scrapyd.cn/doc/)
* [Scrapy实战_Scrapy 中文网](http://www.scrapyd.cn/example/)
* [scrapy爬虫框架教程（一）-- Scrapy入门 - 云+社区 - 腾讯云](https://cloud.tencent.com/developer/article/1095148)
* [Scrapy爬虫框架教程（二）-- 爬取豆瓣电影TOP250 - 云+社区 - 腾讯云](https://cloud.tencent.com/developer/article/1095181)
* [Scrapy爬虫框架教程（三）-- 调试(Debugging)Spiders - 云+社区 - 腾讯云](https://cloud.tencent.com/developer/article/1095201)
* [Scrapy爬虫框架教程（四）-- 抓取AJAX异步加载网页 - 云+社区 - 腾讯云](https://cloud.tencent.com/developer/article/1095216)
* [scrapy爬虫系列：如何使用pycharm调试scrapy程序](https://newsn.net/say/scrapy-debug.html)
* [Scrapy爬虫(十)：爬虫总结以及扩展 - 李燕西的博客 - CSDN博客](https://blog.csdn.net/yancey_blog/article/details/53907613)
* [Scrapy爬虫(九)：scrapy的调取网易云音乐 - 后端 - 掘金](https://juejin.im/entry/59e8b0e8f265da43070263ba)
* [Python：Scrapy Shell的使用试技巧 - 李燕西的博客 - CSDN博客](https://blog.csdn.net/yancey_blog/article/details/53907215)
* [Python爬虫(13):Scrapy实战抓教程 - 曾是土木人 - CSDN博客](https://blog.csdn.net/php_fly/article/details/19555969)
* [Scrapy的架构 - 简书](https://www.jianshu.com/p/335ce3435a2b)





