"""
  作者：LCQT
  日期：2023年05月03日22:39
  项目描述：在派生类当中调用的——init——()方法定义类属性
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
class Sapodilla(Fruit):   # 子类
    def __init__(self,color):
        print('\n我是人参果')
        super().__init__(color)   # 调用基类的构造方法
    def harvest(self,color):
        print('人参果是：', color + '的！')
        print('人参果已经收获......')
        print('人参果原来是：', Fruit.color + '的！')
apple = Apple()   # 创建苹果类的实例
apple.harvest(apple.color)  # 调用harvest（）方法
sapodilla = Sapodilla('白色')
sapodilla.harvest('金黄色带紫色条纹')  # 调用harvest（）方法