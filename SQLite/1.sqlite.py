"""
  作者：LCQT
  日期：2023年05月06日11:40
  项目描述：创建SQLite数据库文件
"""
# 导入模块
import sqlite3
# 创建连接对象
conn = sqlite3.connect('lcqt.db')  # db表明这是一个数据库文件
# 创建游标对象
cursor = conn.cursor()
# 执行SQL语句
cursor.execute('create table user(id int(10) primary key, name varchar(20))')
# 关闭游标
cursor.close()
# 关闭连接
conn.close()