"""
  作者：LCQT
  日期：2023年06月06日17:42
  项目描述：通过输入操作代替识别功能，使用python标准库datetime实现计费，利用循环和分支语句实现自动收费计算
"""
# 停车场自动收费系统
import datetime  # time是python自带的时间库
car_list = []
blank = 16 # 车库最多存放16辆车
in_now_time = 0
while True:
    result = input("是否是进入停车场(y/n)：")
    if result == "y":
        # 进车时
        if blank == 0 :  # 判断车库是否存满
            print("车库已存满，暂无空位！")
            blank = 0
        else:
            car = input("请输入车进入的车牌号：")
            car_dic = {}
            in_now_time = datetime.datetime.now()
            new_now_time = in_now_time.strftime("%y-%m-%d %H: %M: %S") # 去掉毫秒数
            # print(now_time)
            car_dic["车牌"] = car
            car_dic["进入时间"] = new_now_time
            car_list.append(car_dic)
            blank -= 1
            print("当前剩余车位为: {}，车牌为：{}，进入时间为：{}".format(blank,car,new_now_time))
    else:
        # 出站时
        status = False  # 车出停车场状态
        out_car = input("请输入车出去的车牌号：")
        # 判断本车是否录入过进门信息
        for car in car_list:
            if car["车牌"] == out_car:
                # 计算停车时间
                in_time = car["进入时间"]
                # 获取相差秒
                get_second = (datetime.datetime.now() - in_now_time).seconds
                # house = get_second /60/60 +4 调试，+几表示你延后多久
                house = get_second /60/60
                # 判断停留时间
                if house <= 2:  # 两小时内不收费
                    print("停车未满2小时，本次免费，欢迎下次光临！")
                    car_list.remove(car)
                    blank += 1
                elif 2 < house <= 4:
                    print("本次停车时间为：{: .3f}小时,收费10元！欢迎下次光临".format(house))
                    car_list.remove(car)
                    blank += 1
                elif 4 < house <= 6:
                    print("本次停车时间为：{: .3f}小时,收费15元！欢迎下次光临".format(house))
                    car_list.remove(car)
                    blank += 1
                elif 6 < house <= 8:
                    print("本次停车时间为：{: .3f}小时,收费20元！欢迎下次光临".format(house))
                    car_list.remove(car)
                    blank += 1
                elif 8 < house <= 10:
                    print("本次停车时间为：{: .3f}小时,收费25元！欢迎下次光临".format(house))
                    car_list.remove(car)
                    blank += 1
                else:
                    print("本次停车时间为：{: .3f}小时,收费30元！欢迎下次光临".format(house))
                    car_list.remove(car)
                    blank += 1
                status = True

        if status != True:
            print("请联系停车场管理员，本车辆未记录信息，不允许出停车场")
            continue