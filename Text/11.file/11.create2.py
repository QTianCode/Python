"""
  作者：LCQT
  日期：2023年05月05日16:19
  项目描述：
"""
import os
# 创建目录，如果目录已存在会抛错，并且mkdir无法创建多级目录
# 可以先判断目录是否已存在
def mkdir(path):    # 创建一个递归函数用于创建目录
    if not os.path.isdir(path):   # 判断是否为路径
        mkdir(os.path.split(path)[0])
    else:
        return
    os.mkdir(path)
mkdir('D:\\PycharmProjects\\pythonProject\\Text\\11.file\\demo\\test\\demo')
