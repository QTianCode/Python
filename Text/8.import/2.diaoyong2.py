"""
  作者：LCQT
  日期：2023年05月04日10:18
  项目描述：调用同名定义模块
"""
import fang
import r
if __name__ == '__main__':
    print('圆的周长为：', r.girth(20))
    print('矩形的周长为：', fang.girth(30,40))
    print('圆的面积为：', r.area(20))
    print('矩形的面积为：', fang.area(30, 40))