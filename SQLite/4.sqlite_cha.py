"""
  作者：LCQT
  日期：2023年05月06日15:47
  项目描述：
"""
# 导入模块
import sqlite3
# 创建连接对象
conn = sqlite3.connect('lcqt.db')  # db表明这是一个数据库文件
# 创建游标对象
cursor = conn.cursor()
# 执行SQL语句
sql = 'select * from user where id >2'
cursor.execute(sql)
# cursor.fetchone()
# cursor.fetchone()
# result1 = cursor.fetchmany(5)
result1 = cursor.fetchall()
print(result1)
# 关闭游标
cursor.close()
# 提交事物  查询不需要提交事物
# conn.commit()
# 关闭连接
conn.close()