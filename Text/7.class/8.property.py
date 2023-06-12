"""
  作者：LCQT
  日期：2023年05月03日16:27
  项目描述：创建用于计算的属性
"""
class Rect:
    def __init__(self,width,height):  # 构造方法
        self.width = width   # 矩形的宽度
        self.height = height  # 矩形的高度
    @property
    def area(self):
        return self.width*self.height  # 计算矩形面积
rect = Rect(800,600)
print('面积为：', rect.area)
