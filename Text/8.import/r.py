"""
  作者：LCQT
  日期：2023年05月04日10:11
  项目描述：计算圆的周长和面积
"""
import math
PI =math.pi
def girth(r):
    '''计算圆周长的函数'''
    return round(2*PI*r, 1)
def area(r):
    '''计算圆面积的函数'''
    return round(PI*r*r, 1)
if __name__ == '__main__':
    print(area(10))