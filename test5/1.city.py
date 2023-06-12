"""
  作者：LCQT
  日期：2023年06月07日14:01
  项目描述：查询城市所在的省份
"""


def find_city(test):
    pro = ["广东", "四川", "贵州", "不存在"]
    city = [["广州", "深圳", "惠州", "珠海"], ["成都", "内江", "乐山"], ["贵阳", "六盘水", "遵义"]]

    for i, province_cities in enumerate(city):
        if test in province_cities:
            print(i)
            return pro[i]

    return pro[-1]  # Return "不存在" if the city name is not found in the list


while True:
    test = input('请输入查询的城市名称：')
    city = find_city(test)
    print('查询结果：', city)
