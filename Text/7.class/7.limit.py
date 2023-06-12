"""
  作者：LCQT
  日期：2023年05月03日16:19
  项目描述：访问限制
"""
class Swan:
    '''天鹅类'''
    __neck_swan = '天鹅的脖子很长'   # 私有类型的属性
    def __init__(self):
        print('__init__:',Swan.__neck_swan)  # 在实例方法中访问
swan = Swan()  # 创建Swan类的实例   swan 为实例名
print('通过实例名访问：',swan._Swan__neck_swan)   # 通过实例名访问