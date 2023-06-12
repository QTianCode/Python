"""
  作者：LCQT
  日期：2023年05月06日17:26
  项目描述：连接数据库，不同版本的connect内部不同
"""
# 导入pymysql模块
import pymysql
# 调用connect()函数生成connection连接对象
db = pymysql.connect(host='localhost', user='root', password='20000819', db='zhenhua')
# 调用cursor()方法，创建Cursor对象
cursor = db.cursor()
# 执行SQL语句
cursor.execute('select version()')  # 查询版本信息
data = cursor.fetchone()
print(data)
# 关闭连接
cursor.close()
db.close()
