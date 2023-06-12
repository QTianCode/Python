"""
  作者：LCQT
  日期：2023年05月06日15:38
  项目描述：
"""
# 导入模块
import sqlite3
# 创建连接对象
conn = sqlite3.connect('database.db')  # db表明这是一个数据库文件
# 创建游标对象
cursor = conn.cursor()
# 执行SQL语句
# (3)执行DDL（Data Definition Language）语句创建数据表
sql = '''create table user_tb(
    _id integer primary key autoincrement,
    name text,
    pass text,
    gender text)'''
cursor.execute(sql)
# 关闭游标
cursor.close()
# 提交事物
conn.commit()
# 关闭连接
conn.close()


