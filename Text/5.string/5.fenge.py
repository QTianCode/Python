"""
  作者：LCQT
  日期：2023年05月01日11:09
  项目描述：使用正则表达式分割字符串
"""
import re
str1 = '葛鑫怡 张婧仪 田曦薇 庄达菲 章若楠 宋雨琦 陈昊宇 赵今麦 李兰迪 谭松韵 吕小雨'
pattern = r'\s'   # *表示匹配前面的字符零次或多次
list = re.split(pattern, str1)
print("您喜欢的艺人有：")
for i in list:
    if i != "":
        print(i)

