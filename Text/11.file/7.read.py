"""
  作者：LCQT
  日期：2023年05月05日14:49
  项目描述：
"""
print('\n', '='*10, '我真的很帅', '='*10)
with open('ing.txt', 'r') as file:   # 打开文件
    line = file.readlines()
    for i in line:
        print(i)
print('\n', '='*29, 'over', '='*29, '\n')


# line = file.read()  # 读取全部信息

#number = 0  # 记录行号
#while True:
#    number += 1
#    line = file.readline()  # 逐行读取，防止一次性读取太多，内存不足
#    if line == '':
#        break  # 跳出循环
#    print(line)  # 输出一行