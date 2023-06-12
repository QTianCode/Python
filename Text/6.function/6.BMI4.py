"""
  作者：LCQT
  日期：2023年05月03日00:35
  项目描述：计算列表里的BMI
"""
def fun_bmi(*person):   # *代表可变参数
    '''
    功能：根据身高和体重计算BMI指数
    :param person: 人名  height: 身高（单位：米） weight: 体重（单位：千克）
    :return:
    '''
    for list_person in person:
        for item in list_person:
            person = item[0]
            height = item[1]
            weight = item[2]
            print(person + '的身高' + str(height) + '米 \t 体重：' + str(weight) + '千克')

            bmi = weight/(height * height)  # 用于计算BMI值
            print('您的BMI指数为：' + str(bmi))
            # 判断身材是否合理
            if bmi < 18.5:
                print('您的体重过轻=-=')
            if bmi >= 18.5 and bmi < 24.9:
                print('您的体重正常，请保持！^-^')
            if bmi >= 24.9 and bmi < 29.9:
                print('您的体重过重=-=')
            if bmi >= 29.9:
                print('您属于肥胖，请减肥！')
# 调用函数
list_w = [['大帅哥',1.76, 60], ['佩奇', 1.3, 40], ['我超帅', 1.83, 89]]
list_m = [['喜羊羊', 1.6, 60],['美羊羊', 1.55, 45]]
fun_bmi(list_w, list_m)