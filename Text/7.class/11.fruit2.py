"""
  作者：LCQT
  日期：2023年05月03日22:23
  项目描述：方法重写
"""
class Fruit:     # 基类
    color = '绿色'
    def harvest(self,color):
        print('水果是：', color +'的！')
        print('水果已经收获......')
        print('水果原来是：', Fruit.color +'的！')
class Apple(Fruit):   # 子类
    color = '红色'
    def __init__(self):
        print('我是苹果')
    def harvest(self,color):
        print('苹果是：', color+ '的！')
        print('苹果已经收获......')
        print('苹果原来是：', Fruit.color + '的！')
class Orange(Fruit):   # 子类
    color = '橙色'
    def __init__(self):
        print('我是橘子')
    def harvest(self,color):
        print('橘子是：', color + '的！')
        print('橘子已经收获......')
        print('橘子原来是：', Fruit.color + '的！')
apple = Apple()
apple.harvest(apple.color)  # 调用基类的harvest（）方法
orange = Orange()
orange.harvest(orange.color)  # 调用基类的harvest（）方法