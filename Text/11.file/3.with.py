"""
  作者：LCQT
  日期：2023年05月05日14:25
  项目描述：用with语句打开文件
"""
print('\n', '='*10, '我真的很帅', '='*10)
with open('message.txt', 'a+', encoding= 'UTF-8') as file:   #打开文件
    pass
print('即将显示......')
print('关闭了吗：', file.closed)
