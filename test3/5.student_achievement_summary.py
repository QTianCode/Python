"""
  作者：LCQT
  日期：2023年06月06日10:33
  项目描述：基于字典模型，统计学生成绩
"""
# 字典形成存储了英语、语文、数学的成绩
English = {'张三': 85, '李四': 62, '王五': 96}
Math = {'李四': 66, '王五': 91, '赵六': 76}
Chinese = {'张三': 85, '李四': 62}
s = list(English.keys()) + list(Math.keys()) + list(Chinese.keys())  # 将所有姓名放到列表
s = set(s)  # 通过集合的方式去重
s = list(s)  # 转换为列表方便读取
print("{: <{}}  {: <{}} {: <{}} {: <{}}".format('科目', 8, 'English', 8, 'Math', 8, 'Chinese', 8))
for i in s:
    print("{: <{}}  {: <{}} {: <{}} {: <{}}".format(i, 8, English.get(i, 'NaN'), 8, Math.get(i, 'NaN'), 8,
                                                    Chinese.get(i, 'NaN'), 8))  # 上下在同一行，format方式指定宽度8