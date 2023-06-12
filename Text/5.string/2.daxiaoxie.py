# 开发者 : 晴天
# 开发日期 : 2023/4/25
# 字符串大小写转换
# 区分大小写
username = 'Clearlove|MLXG|UZI|LWX|xiaohu'
rgname1 = input('请输入要注册的ID:')
rgname2 = '|'+rgname1 +"|"
if rgname2 in username:
    print(rgname2,'ID已存在')
else:
    print(rgname2,'ID可以注册')
