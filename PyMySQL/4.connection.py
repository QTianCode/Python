"""
  作者：LCQT
  日期：2023年05月09日13:07
  项目描述：获取连接对象
"""
import pymysql

try:
    connection = pymysql.connect(
    host = 'localhost', # 主机名
    user = 'root',      # 数据库用户名
    password = '20000819',  # 数据库密码
    db = 'bayuechangan',      # 数据库名
    charset = 'utf8',   # 字符集编码
    cursorclass = pymysql.cursors.DictCursor # 游标类型
)
    print(connection)
except Exception as e:
    print(e)

# SQL语句
# NOT NULL 非空
# AUTO_INCREMENT 自动编号
# default values  设置默认值
# primary key 主键
sql = """
CREATE TABLE books (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    category varchar(50) NOT NULL,
    price decimal(10,2) DEFAULT '0',
    publish_time date DEFAULT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
"""
cursor = connection.cursor()  # 获取游标对象
cursor.execute(sql)  # 执行SQL语句
cursor.close()      # 关闭游标
connection.close()  # 关闭连接
