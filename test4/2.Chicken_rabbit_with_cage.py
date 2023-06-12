"""
  作者：LCQT
  日期：2023年06月06日17:22
  项目描述：鸡兔同笼问题
"""
head = int(input('请输入头的总数：'))
jio = int(input('请输入脚的总数：'))
for x in range(1,100):
    y = head - x
    if 2*x + 4*y == jio:
        print('鸡有%s只，兔子有%s只' % (x, y))
