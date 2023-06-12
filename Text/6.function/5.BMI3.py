"""
  作者：LCQT
  日期：2023年05月02日19:53
  项目描述：传入可变参数
"""
def demo(obj=None):    # 定义函数并为参数设置默认值
    if obj == None:
        obj = []
    print('obj的值：', obj)
    obj.append(1)
demo()
demo()

# 在定义一个函数的时候，为一个参数设置默认值，这个参数必须指向一个不可变对象