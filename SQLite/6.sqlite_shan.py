"""
  作者：LCQT
  日期：2023年05月06日16:00
  项目描述：
"""
# 导入模块
import sqlite3
# 创建连接对象
conn = sqlite3.connect('lcqt.db')  # db表明这是一个数据库文件
# 创建游标对象
cursor = conn.cursor()
# 执行SQL语句
# sql = 'delete from user'  #会删掉整个数据库
sql = 'delete from user where id = ?'  # 此处直接用真实值很危险，一般用问号
cursor.execute(sql, (1,))  # 元组只有一个元素时要加逗号
# 关闭游标
cursor.close()
# 提交事物
conn.commit()
# 关闭连接
conn.close()