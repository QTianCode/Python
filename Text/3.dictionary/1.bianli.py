# 开发者 : 晴天
# 开发日期 : 2023/4/24
# 字典遍历
team = ("JDG", 'BLG', 'EDG', 'OMG', 'LNG', 'WBG', 'RNG', 'WE')
name = ('369', 'Yagao', 'Meiko', 'Shanji', 'Tazan', 'Theshy', 'Ming', 'Shanks')
LPL = dict(zip(team,name))
for key,value in LPL.items():
    print(key,'的选手是',value)
for key in LPL.keys():
    print(key)
for value in LPL.values():
    print(value)