"""
  作者：LCQT
  日期：2023年06月06日17:32
  项目描述：1-20随机生成一个数用户有5次猜数机会
"""
import random

max_retry = 5
i = 0
random_num = random.randint(1, 20)
while i < max_retry:
    try:
        num = int(input("请输入1-20的一个数字："))
        # print(f'你输入的数字是 : {num}')
        if num > random_num:
            print('太大')
        elif num < random_num:
            print('太小')
        else:
            print('!!Great,你猜中啦!')
            break
    except Exception as e:
        print('输入不正确！')
    finally:  # 无论try块中的代码是否引发异常，以及异常是否被处理，总是最后执行这里的代码
        i += 1
        print(f'剩余次数: {max_retry - i}')
else:
    print('错误次数超过5次,你输啦!')