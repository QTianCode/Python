"""
  作者：LCQT
  日期：2023年05月05日20:14
  项目描述：重命名文件和目录
"""
import os
# 原路径
scr = r'D:\PycharmProjects\pythonProject\Text\11.file\demo\test\hhh.txt'
# 修改后的路径
dst = r'D:\PycharmProjects\pythonProject\Text\11.file\demo\test\m.txt'
if os.path.exists(scr):
    os.rename(scr, dst)  # 重命名文件
else:
    print('文件不存在。')
# 目录同理
