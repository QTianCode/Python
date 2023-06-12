# 开发者 : 晴天
# 开发日期 : 2023/4/25
# 利用字典推导式创建字典
name = ['meiko', 'yagao', 'theshy', 'lwx']
team = ['EDG', 'BLG', 'WBG', 'FPX']
dict1 = {i:j for i,j in zip(team,name)}
print(dict1)