"""
  作者：LCQT
  日期：2023年06月07日15:30
  项目描述：a+aa+aaa+aaaa....
"""
def func(a,n):
    num = a
    b = a
    for i in range(1,n):
       b += a*(10**i) # i=1时表示十位，i=2时表示百位，以此类推
       num += b
    return num
h = func(2,10)
print(h)