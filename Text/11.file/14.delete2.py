"""
  作者：LCQT
  日期：2023年05月05日19:07
  项目描述：删除不为空的目录
"""
import os, shutil
if os.path.exists(r'D:\PycharmProjects\pythonProject\text\11.file\first'):
    # emdir没办法删除非空目录
    shutil.rmtree('D:\\PycharmProjects\\pythonProject\\text\\11.file\\first')
else:
    print('目录不存在')
