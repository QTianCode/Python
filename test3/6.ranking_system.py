"""
  作者：LCQT
  日期：2023年06月06日10:39
  项目描述：使用Python数据存储模型、字典、列表特性对学生成绩进行记录和排序，并格式化输出
"""
num = input("请输入你要录入的学生成绩数量：")
i = 0
print("输入学生名和三科总成绩格式如：张三，289")
stu = {}
# 添加学生信息
while i < int(num):
    student_info = input("请输入学生名和总成绩：")
    student_info_list = student_info.split("，")
    stu[student_info_list[0]] = int(student_info_list[1])   # 列表中的第一个元素代表学生姓名，第二个元素代表学生成绩
    i += 1
# 字典排序
new_stu = sorted(stu.items(), key=lambda d: d[1], reverse=True)
# # 显示学生信息
j = 0
print("{: ^10}\t{: ^6}\t{: ^8}".format("姓名", "总成绩", "排名", chr(12288)))
while j < len(new_stu):
    print("{: ^10}\t{: ^6}\t{: ^16}".format(
        new_stu[j][0], new_stu[j][1], j + 1, chr(12288)))
    j += 1
