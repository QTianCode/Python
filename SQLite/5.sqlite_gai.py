"""
  作者：LCQT
  日期：2023年05月06日15:52
  项目描述：
"""
# 导入模块
import sqlite3
# 创建连接对象
conn = sqlite3.connect('lcqt.db')  # db表明这是一个数据库文件
# 创建游标对象
cursor = conn.cursor()
# 执行SQL语句
sql = 'update user set name = ? where id = ?'  # 此处直接用真实值很危险，一般用问号
cursor.execute(sql, ('林杨', 2))
# 关闭游标
cursor.close()
# 提交事物
conn.commit()
# 关闭连接
conn.close()
