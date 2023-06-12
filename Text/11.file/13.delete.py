"""
  作者：LCQT
  日期：2023年05月05日18:56
  项目描述：删除目录
"""
import os
if os.path.exists(r'D:\PycharmProjects\pythonProject\text\11.file\first\second\thirst'):
    # emdir没办法删除非空目录
    os.rmdir('D:\\PycharmProjects\\pythonProject\\text\\11.file\\first\\second\\thirst')
else:
    print('目录不存在')
