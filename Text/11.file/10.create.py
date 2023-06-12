"""
  作者：LCQT
  日期：2023年05月05日16:14
  项目描述：创建目录
"""
import os
# 创建目录，如果目录已存在会抛错，并且mkdir无法创建多级目录
# 可以先判断目录是否已存在
if not os.path.exists('D:\\PycharmProjects\\pythonProject\\Text\\11.file\\demo'):
    os.mkdir('D:\\PycharmProjects\\pythonProject\\Text\\11.file\\demo')
else:
    print('该目录已存在')