# 开发者 : 晴天
# 开发日期 : 2023/4/23
# 统计函数
team = ['EDG', 'JDG', 'BLG', 'IG', 'EDG', 'OMG']
number = team.count('EDG')  # 统计元素出现的次数
print(number)
position = team.index('EDG')   # 统计元素首次出现的下标
print(position)
score = [99,67,56,43,75,82]
total = sum(score)/len(score)
print(total)