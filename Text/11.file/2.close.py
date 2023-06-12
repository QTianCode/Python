"""
  作者：LCQT
  日期：2023年05月05日14:15
  项目描述：
"""
print('\n', '='*10, '我真的很帅', '='*10)
file = open('message.txt', 'a+', encoding= 'UTF-8')
print('\n即将显示......')
print(file.read()) # 读取文件
print('关闭前：', file.closed)
file.close()
print('关闭后：', file.closed)