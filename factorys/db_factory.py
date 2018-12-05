# comment: 数据库工厂, 生产表实例
import conf
from sql_factory import SqliteFactory

db_factory = SqliteFactory("database")
csdn_article_table = db_factory.db("Spider", conf.db_path).table("CsdnArticle")
