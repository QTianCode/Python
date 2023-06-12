"""
  作者：LCQT
  日期：2023年06月07日12:32
  项目描述：正数输出1，负数输出-1，其他值输出0
"""

try:
    i = float(input('请输入一个整数：'))
    if i > 0:
        print('1')
    elif i < 0:
        print('-1')
    else:
        print('0')
except ValueError as V:
    print('您输入的值类似不对，请重新输入')