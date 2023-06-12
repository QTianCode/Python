"""
  作者：LCQT
  日期：2023年05月05日14:42
  项目描述：
"""
list1 = ['易建联', '博尔特', '姆巴佩', '张怡宁']
with open('sporter.txt', 'w') as file:
    file.writelines([line + '\t' for line in list1])