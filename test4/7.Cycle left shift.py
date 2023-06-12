"""
  作者：LCQT
  日期：2023年06月07日12:26
  项目描述：20个随机数循环左移
"""
import random
l = [random.randint(0,50) for i in range(20)]
print(l)
for i in range(5):
   l.append(l.pop(0))
print(l)