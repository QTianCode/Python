# 开发者 : 晴天
# 开发日期 : 2023/4/23
# 列表添加
oldphone = ["诺基亚", "联想", '酷派']
phone = ["华为", '三星', "苹果", 'OPPO']
phone.append("Vivo")
print(phone)
phone.insert(1, "荣耀")
print(phone)
oldphone.extend(phone)       # 把列表元素加到另一个列表上
print(oldphone)
oldphone[1] = "乐视"          # 通过索引修改列表元素
print(oldphone)
del oldphone[2]              # 通过索引删除列表元素
print(oldphone)
del oldphone[-1]
print(oldphone)
oldphone.remove("乐视")       # 根据值删除列表元素
print(oldphone)