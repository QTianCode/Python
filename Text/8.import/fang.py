"""
  作者：LCQT
  日期：2023年05月04日10:15
  项目描述：计算矩形的周长和面积
"""
def girth(width, height):
    '''计算矩形周长的函数'''
    return 2*(width+height)
def area(width, height):
    '''计算圆面积的函数'''
    return width*height
if __name__ == '__main__':
    print(area(10, 20))