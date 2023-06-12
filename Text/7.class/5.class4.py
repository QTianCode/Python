"""
  作者：LCQT
  日期：2023年05月03日15:32
  项目描述：创建数据成员并访问
"""
class Geese:
    '''大雁类'''
    neck = '脖子较长'  # 类属性（脖子）
    wing = '振翅频率高'  # 类属性（翅膀）
    leg = '腿位于身体的中心支点，行走自如'  # 类属性（腿）
    number = 0
    def __init__(self):   # self必须作为init方法的第一个参数，有其他参数可以在后边用逗号添加
        Geese.number += 1
        print('\n我是第%d大雁，我属于雁类，我有以下特征：'%Geese.number)   # 格式化字符串
        print(Geese.neck)  # 脖子
        print(Geese.wing)  # 翅膀
        print(Geese.leg)  # 腿

list1 = []
for i in range(4):  # 循环四次
    if i == 1:
        Geese.beak = '喙的基部较高，长度和头部几乎相等'  # 添加类属性
        list1.append(Geese())
        print(list1[1].beak)    # 第二只大雁的喙的特征
    else:
        list1.append(Geese())   # 创建大雁类的实例
print('\n一共有%d只大雁!'%Geese.number)

