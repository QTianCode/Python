"""
  作者：LCQT
  日期：2023年05月05日20:02
  项目描述：删除文件（不能删除目录）
"""
import os
if os.path.exists(r'D:\PycharmProjects\pythonProject\Text\11.file\demo\test\demo\wwww.txt'):
    os.remove(r'D:\PycharmProjects\pythonProject\Text\11.file\demo\test\demo\wwww.txt')
else:
    print('文件不存在。')
