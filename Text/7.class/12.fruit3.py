"""
  作者：LCQT
  日期：2023年05月03日22:29
  项目描述：派生（子类）类中调用基类的——init——()方法
"""
class Fruit:     # 基类
    def __init__(self, color='绿色'):
        Fruit.color = color  # 类属性

    def harvest(self,color):
        print('水果是：', color +'的！')
        print('水果已经收获......')
        print('水果原来是：', Fruit.color +'的！')
class Apple(Fruit):   # 子类
    color = '红色'
    def __init__(self):
        print('我是苹果')
        super().__init__()   # 调用基类的构造方法
    def harvest(self,color):
        print('苹果是：', color+ '的！')
        print('苹果已经收获......')
        print('苹果原来是：', Fruit.color + '的！')
class Orange(Fruit):   # 子类
    color = '橙色'
    def __init__(self):
        print('我是橘子')
        super().__init__()   # 调用基类的构造方法
    def harvest(self,color):
        print('橘子是：', color + '的！')
        print('橘子已经收获......')
        print('橘子原来是：', Fruit.color + '的！')
apple = Apple()
apple.harvest(apple.color)  # 调用基类的harvest（）方法
orange = Orange()
orange.harvest(orange.color)  # 调用基类的harvest（）方法