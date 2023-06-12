"""
  作者：LCQT
  日期：2023年05月06日17:53
  项目描述：
"""
# 导入pymysql模块
import pymysql
# 调用connect()函数生成connection连接对象
db = pymysql.connect(host='localhost', user='root', password='20000819', db='zhenhua')
# 调用cursor()方法，创建Cursor对象
cursor = db.cursor()
# cursor.execute('drop table if exists books')  # 如果表已存在，则删除原表
# 执行SQL语句    创建一个表
sql = '''
create TABLE books(                              
      id int(8) NOT NULL AUTO_INCREMENT,
      name varchar(50) NOT NULL,
      category varchar(50) NOT NULL,
      price decimal(10,2) DEFAULT NULL,
      publish_time date DEFAULT NULL,
      PRIMARY KEY (id)
)ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
'''
cursor.execute(sql)
# 关闭连接
cursor.close()
db.close()