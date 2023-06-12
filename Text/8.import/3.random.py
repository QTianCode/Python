"""
  作者：LCQT
  日期：2023年05月04日19:17
  项目描述：如何利用random模块创建一个随机的验证码
"""
import random
if __name__ == '__main__':
    checkcode = ''   # 保存验证码的变量
    for i in range(4):
        index = random.randrange(0, 4)  # 生产一个0~3中的一个数
        if index != i and index +1 != i:
            checkcode += chr(random.randint(97,122)) # 生成a~z中的一个小写字母
        elif index +1 ==i:
            checkcode += chr(random.randint(65, 90))  # 生成A~Z中的一个大写字母
        else:
            checkcode += str(random.randint(1, 9))  # 生成1~9中的一个数字
    print(checkcode)