"""
  作者：LCQT
  日期：2023年06月06日09:58
  项目描述：根据集合的特性，将重复下载文件名去掉
"""
# 下载去重器
# 下载集合
download = set()
file_name1 = input("请输入你要下载的文件名: ")
file_name2 = input("请输入你要下载的文件名: ")
file_name3 = input("请输入你要下载的文件名: ")
download.add(file_name1)
download.add(file_name2)
download.add(file_name3)
i = 0
# len() 获取集合个数
print("下载提示：")
while i < len(download):
    print("{}文件已下载...".format(tuple(download)[i]))
    i += 1