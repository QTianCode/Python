"""
  作者：LCQT
  日期：2023年06月06日16:26
  项目描述：
"""
score = int(input('请输入分数：'))
grade = ''
if score < 60:
    grade = '不及格'
if 60 <= score < 80:
    grade = '及格'
if 80 <= score < 90:
    grade = '良好'
else:
    grade = '优秀'
print('分数是{0},等级是{1}'.format(score, grade))