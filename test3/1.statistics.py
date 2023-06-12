"""
  作者：LCQT
  日期：2023年06月05日23:52
  项目描述：统计字符串中数字和字母的个数
"""
s = input('请输入字符串：')
dic = {'letter': 0, 'integer': 0, 'space': 0, 'other': 0}
for i in s:
    if i > 'a' and i < 'z' or i > 'A' and i < 'Z':  # 比较ASCII码值
        dic['letter'] += 1
    elif i in '0123456789':
        dic['integer'] += 1
    elif i == ' ':
        dic['space'] += 1
    else:
        dic['other'] += 1
print('统计字符串：', s)
print(dic)
