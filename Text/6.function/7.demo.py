"""
  作者：LCQT
  日期：2023年05月03日00:52
  项目描述：**parameter  接收任意多个类似关键字参数一样的显式赋值的实际参数，并将其放到一个字典中。
"""
def sign(**sign):
    print()
    for key,value in sign.items(): # 遍历字典
        print(key,'的星座是：', value)
#sign(绮梦 = '水瓶座', 冷一一 = '射手座')
#sign(香凝 = '双鱼座', 黛蓝 = '天蝎座')
dict = {'香凝' : '双鱼座', '黛蓝' : '天蝎座'}   # 创建字典要用大括号和冒号
sign(**dict)
