"""
  作者：LCQT
  日期：2023年05月09日13:45
  项目描述：
"""
import pymysql
# 打开数据库连接   # 字符集编码,使用connect()方法时，需要额外设置字符集 charset = UTF8,防止插入中文时出错。
connection = pymysql.connect(host='localhost', user='root',password= '20000819', db='bayuechangan', charset='utf8')
cursor = connection.cursor()  # 获取游标对象
# 数据列表
data = [('你好旧时光', '实体小说', '128', '2009.12.1'), ('暗恋橘生淮南', '网络小说', '528', '2012.11.11'), ('最好的我们', '实体小说', '188', '2013.5.20'), ('这么多年', '番外小说', '168', '2023.4.28'),]

# 执行SQL语句，插入多条记录  使用insert语句插入数据时，使用%s可以防止SQL注入。
try:
    cursor.executemany('insert into books(name, category, price, publish_time) values(%s, %s, %s, %s)', data)
    connection.commit()  # 提交数据
except:
# 发生错误回滚
    connection.rollback()

# 关闭数据库连接
connection.close()


