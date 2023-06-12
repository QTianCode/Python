"""
  作者：LCQT
  日期：2023年05月06日18:46
  项目描述：往books表中新增数据
"""
# 导入pymysql模块
import pymysql
# 调用connect()函数生成connection连接对象
db = pymysql.connect(host='localhost', user='root', password='20000819', db='zhenhua', charset='utf8')  # 因为用到了中文，所以要设置一个编码格式
# 调用cursor()方法，创建Cursor对象
cursor = db.cursor()
# 多个数据可以用字典的方式传入
data = [('你好旧时光', 'TV', '100', '1999.9.2'), ('最好的我们', 'TV', '100', '1990.5.31'), ('这么多年', 'Movie', '28.9', '1997.4.18')]
try:  # 失败也不会报错
# 执行SQL语句
    sql = 'insert into books(name, category, price, publish_time) values(%s,%s,%s,%s)'
# cursor.execute(sql, data) 加入一条
    cursor.executemany(sql, data)  # 加入多条
    db.commit()
except:
    db.rollback()   # 该rollback()方法用于恢复对数据库所做的最后更改或提交。如果出现用户对数据库更改不满意的情况，或者如果事务失败，
                    # 则rollback()操作该方法以将数据库恢复到其提交更改之前的原始状态。这是一个非常重要的方法，因为它有助于在任何事务失败的情况下维护数据库的完整性。

# 关闭连接
cursor.close()
db.close()