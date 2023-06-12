"""
  作者：LCQT
  日期：2023年05月05日14:30
  项目描述：向文件写入内容
"""
print('\n', '='*10, '我真的很帅', '='*10)
with open('message.txt', 'w', encoding= 'UTF-8') as file:   #打开文件
    file.write('相信自己')
print('即将显示......')
print('关闭了吗:', file.closed)
