"""
  作者：LCQT
  日期：2023年05月09日14:07
  项目描述：
"""
import pymysql
connection = pymysql.connect(
    host = 'localhost', # 主机名
    user = 'root',      # 数据库用户名
    password = '20000819',  # 数据库密码
    db = 'bayuechangan',      # 数据库名
    charset = 'utf8',   # 字符集编码
    cursorclass = pymysql.cursors.DictCursor # 游标类型
)
sql = 'select * from books order by price'   # 把表中数据按价格由低到高排序，逆序则用desc
with connection.cursor() as cursor:
    cursor.execute(sql)
    data = cursor.fetchall()
# 遍历图书资料
for book in data:
    print(f'图书:{book["name"]},价格:{book["price"]}')

connection.close()