# 开发者 : 晴天
# 开发日期 : 2023/4/23
# 二维列表
str1 = '千山鸟飞绝'
str2 = '万径人踪灭'
str3 = '孤舟蓑笠翁'
str4 = '独钓寒江雪'
list1 = [list(str1), list(str2), list(str3), list(str4)]
print('\n---横板---\n')
for i in range(4):     # 循环古诗的行
    for j in range(5):    # 循环每一行的字
        if j == 4:        # 一行中的最后一个字
            print(list1[i][j])     # 换行输出
        else:
            print(list1[i][j],end='')     # 不换行输出

print('\n---竖版---\n')
list1.reverse()    # 进行逆序排序
print(list1)
for i in range(5):  # 循环每一行中的每一个
   for j in range(4):    # 每一行
        if j==3:        # 每一行最后一个
            print(list1[j][i])    # 换行输出
        else:
            print(list1[j][i], end='')  # 不换行输出