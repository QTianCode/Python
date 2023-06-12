"""
  作者：LCQT
  日期：2023年06月06日16:01
  项目描述：生成包含20个随机数的列表，然后将前10个元素按升序排列，后十个元素按降序排列
"""
import random
i = [random.randint(1,100) for w in range(20)]
print(sorted(i[:10]) + sorted(i[10:], reverse=True))
