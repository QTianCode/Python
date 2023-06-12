"""
  作者：LCQT
  日期：2023年05月05日15:43
  项目描述：目录相关操作
"""
import os
# 判断目录/文件是否存在，目录不区分大小写
print(os.path.exists('D:\\PycharmProjects\\pythonProject\\Text\\11.file\\9.path.py'))


# 拼接路径  拼接时如果出现多个拼接路径，以最后一个出现的为准
# print(os.path.join('D:\\PycharmProjects\\pythonProject\\Text\\11.file\\something\\some.txt'))

# 相对路径
# print(os.getcwd())
# with open('something\\some.txt') as file:  # 通过相对路径打开文件
    # print(file.read())

# print(os.path.abspath('something\\some.txt'))   # 绝对路径