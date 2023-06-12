"""
  作者：LCQT
  日期：2023年06月07日20:02
  项目描述：用户名注册验证系统
"""
import re
# 验证用户名
# 用户名在8-16为之中
# 数组、字母、下划线和-!@#$%&*特殊符号
def checking_username1(data):          # 检查函数
    rule = "^[\w,-,!,@,#,$,%,&,*]{8,16}$"
    result = re.match(rule, data)
    return result

# 用户名中必须由特殊符号和（数组、字母、下划线的至少一种）构成
def checking_username2(data):          #
    normal_num = 0  # 正常数量
    special_num = 0  # 特殊数量
    rule_normal = "[\w]"
    rule_special = '[-!@#$%&*]'
    for i in data:
        if re.search(rule_normal, i):
            normal_num += 1
        elif re.search(rule_special, i):
            special_num += 1
    if normal_num >= 1 and special_num >= 1:
        return data

name_list = []
while True:
    print("""
    1.用户名在8-16位之中
    2.数字、字母、下划线和-!@#$%&*特殊符号
    3.用户名中必须由特殊符号和（数字、字母、下划线的至少一种）构成
    """)
    username = input("请输入用户名：")
    if username:
        print("用户名不为空--已验证...")
        data = checking_username1(username)
        if data:
            print("用户名在8-16的数组、字母、下划线和-!@#$%&*特殊符号--已验证")
            result = checking_username2(username)
            if result:
                print("用户名中必须由特殊符号和（数组、字母、下划线的至少一种）构成--已验证")
                if username not in name_list:  # 验证是否被注册过
                    name_list.append(username)
                    print("*" * 20)
                    print("恭喜你，你输入的用户名可用！")
                else:
                    print("你注册的用户名已存在，请重新注册")
                    continue
            else:
                print("用户名不符合规则，请重新输入")
                continue
        else:
            print("用户名不符合规则，请重新输入")
            continue
    else:
        print("用户名不能为空,请重新输入...")
        continue
