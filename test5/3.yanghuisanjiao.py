"""
  作者：LCQT
  日期：2023年06月07日14:44
  项目描述：杨辉三角
"""
def yhsj(max):
    n = 0
    row = [1]
    while n < max:
        n += 1
        yield row
        row = [1] + [row[k] + row[k + 1] for k in range(len(row) - 1)] + [1]


y = yhsj(5)
for i in y:
    print(i)
