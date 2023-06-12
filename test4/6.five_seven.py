"""
  作者：LCQT
  日期：2023年06月07日12:22
  项目描述：1000内可以整除5和7的最大整数
"""
list = []
for i in range(1000):
    if i % 5 == 0 and i % 7 == 0:
        list.append(i)
print(max(list))