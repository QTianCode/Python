"""
  作者：LCQT
  日期：2023年05月01日10:48
  项目描述：替换字符串
"""
import re
pattern = r'(傻逼)|(日)|(他妈的)|(666)'  # 模式字符串
about = '6666啊，傻逼，我日你大爷'
match = re.sub(pattern, "*", about)
print(match)