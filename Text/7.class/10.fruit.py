"""
  作者：LCQT
  日期：2023年05月03日20:15
  项目描述：继承
"""
class Fruit:     # 基类
    color = '绿色'
    def harvest(self,color):
        print('水果是：', color, '的！')
        print('水果已经收获......')
        print('水果原来是：', Fruit.color, '的！')
class Apple(Fruit):   # 子类
    color = '红色'
    def __init__(self):
        print('我是苹果')
class Orange(Fruit):   # 子类
    color = '橙色'
    def __init__(self):
        print('我是橘子')
apple = Apple()
apple.harvest(apple.color)  # 调用基类的harvest（）方法
orange = Orange()
orange.harvest(orange.color)  # 调用基类的harvest（）方法