"""
  作者：LCQT
  日期：2023年06月06日09:31
  项目描述：通过列表保存学生信息
"""
# 创建一个空列表，用来保存学生的姓名和成绩
student_score = []
while True:
    name = input("请输入学生姓名（输入q退出）：")
    if name == "q":
        break
    student_score.append([name])  # 每次创建一个新列表元素
    score = input("请输入英语，数学，语文的成绩（用逗号分隔）：")
    student_score[-1].append(score.split(','))  # 将成绩传送给最后生成的列表
    print("学生成绩单为：{}".format(student_score))
print("学生成绩单为：{}".format(student_score))
