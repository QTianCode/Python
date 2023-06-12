# 开发者 : 晴天
# 开发日期 : 2023/4/21
h = True
number = 0
while h:
    if number%3==2 and number%5==3 and number%7==2:
        print("符合标准的数为：",number)
        h = False
    else:
        number += 1
