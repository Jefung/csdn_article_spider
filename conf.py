# comment: 配置文件(数据库文件存放,图片目录)
import os
root_dir = os.path.dirname(__file__)
db_file = "sqlite.db"
db_path = os.path.join(root_dir, db_file)
# db_path = r'数据库文件存放目录'
images_dir = os.path.join(root_dir,"images")
# iamges_dir = r'目录存放目录'