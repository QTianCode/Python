"""
  作者：LCQT
  日期：2023年05月03日10:53
  项目描述：匿名函数
"""
import math
#def circlearea(r):    # 计算面积的函数
#    return math.pi*r*r
#r = 10
#print('半径为', r, '的圆面积为：', circlearea(r))

r = 10
# print(lambda r:math.pi*r*r)    生成的是一个lambda对象
result = lambda r:math.pi*r*r
print(result(r))