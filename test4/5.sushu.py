"""
  作者：LCQT
  日期：2023年06月07日12:16
  项目描述：求小于n的素数
"""
n = int(input('请输入你想要判断的范围n：'))
list = []
for i in range(2,n):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        list.append(i)
print(list)