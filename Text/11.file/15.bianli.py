"""
  作者：LCQT
  日期：2023年05月05日19:10
  项目描述：遍历目录
  root是当前正在遍历的这个文件夹的本身的地址
  dirs是一个list，内容是该文件夹中所以的目录的名字（不包括子目录）
  files是一个list，内容是该文件夹中所有的文件（不包括子目录）
"""
import os
path = r'D:\PycharmProjects\pythonProject\Text\11.file'
print('[', path, ']','目录下包含的文件和目录：')
for root, dirs, files in os.walk(path, topdown= True):   # 遍历指定目录
    for name in dirs:
        print('目录：', os.path.join(root, name))  # 遍历看到的目录
    for name in files:
        print('文件：', os.path.join(root, name))  # 遍历看到的文件