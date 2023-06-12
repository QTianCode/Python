# 开发者 : 晴天
# 开发日期 : 2023/4/25
# 不区分大小写
username1 = 'Clearlove|MLXG|UZI|LWX|xiaohu'
username2 = username1.lower()
rgname1 = input('请输入要注册的ID:')
rgname2 = '|'+ rgname1.lower() +"|"
if rgname2 in username2:
    print(rgname2,'ID已存在')
else:
    print(rgname2,'ID可以注册')