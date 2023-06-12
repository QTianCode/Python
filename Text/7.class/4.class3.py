"""
  作者：LCQT
  日期：2023年05月03日15:24
  项目描述：创建实例方法并访问
"""
class Geese:
    '''大雁类'''
    def __init__(self, beak, wing, claw):   # self必须作为init方法的第一个参数，有其他参数可以在后边用逗号添加
        print('我是大雁类，我有以下特征：')
        print(beak)  # 喙
        print(wing)  # 翅膀
        print(claw)  # 爪子
    def fly(self, state = '我会飞'):   # 飞行方法
        print(state)
beak_1 = '喙的基部较高，长度和头的长度几乎相等'
wing_1 = '翅膀长而尖'
claw_1 = '爪子是蹼状的'
wildGoose = Geese(beak_1, wing_1, claw_1)   # 创建大雁类的一个实例
wildGoose.fly('我飞行的时候，一会拍成人字，一会排成一字。')
wildGoose.fly()