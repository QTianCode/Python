"""
  作者：LCQT
  日期：2023年05月03日16:09
  项目描述：实例属性
"""
class Geese:
    '''大雁类'''
    def __init__(self):
        self.neck = '脖子较长'  # 实例属性（脖子）
        self.wing = '振翅频率高'  # 实例属性（翅膀）
        self.leg = '腿位于身体的中心支点，行走自如'  # 实例属性（腿）
        print('我属于雁类，我有以下特征：')
        print(self.neck) # 访问实例属性
        print(self.wing)
        print(self.leg)
geese = Geese()   # 实例化类的对象
geese1 = Geese()
geese1.leg = '通过腿我可以行走'      # 实例属性修改某一个对象的不影响其他对象
print('geese:', geese.leg)
print('geese1:', geese1.leg)  # 实例属性只能通过类的对象来进行访问，不能通过类名称访问