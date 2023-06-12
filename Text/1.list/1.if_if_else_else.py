# 开发者 : 晴天
# 开发日期 : 2023/4/21
print("喝酒不开车，开车不喝酒！\n")
number = int(input("请输入每100毫升的血液酒精数：\n"))

if number >= 20:
    if 80 > number >= 20:
        print("已达酒后驾驶标准，请不要开车！")
    else:
        print("您已达醉驾标准，千万不要开车！")
else:
    print("您还未构成酒驾标准，请小心开车！")
