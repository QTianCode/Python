# 开发者 : 晴天
# 开发日期 : 2023/4/23
# 遍历列表
print("2022-2023LPL春季赛季后赛排名")
team = ["JDG", 'BLG', 'EDG', 'OMG', 'LNG', 'WBG', 'RNG', 'WE']
for index,item in enumerate(team):
    if index % 2 == 0:
        print(index+1, item + '\t\t', end='')
    else:
        print(index+1, item + '\n')