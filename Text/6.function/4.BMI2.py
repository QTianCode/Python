"""
  作者：LCQT
  日期：2023年05月02日19:48
  项目描述：为参数设置默认值
"""
def fun_bmi(height, weight, person = '路人'):   # 此时person使用默认值，默认值必须放在所有参数后
    '''
    功能：根据身高和体重计算BMI指数
    :param person: 人名
    :param height: 身高（单位：米）
    :param weight: 体重（单位：千克）
    :return:
    '''
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

fun_bmi(1.75, 65)
fun_bmi(1.83, 80, '帅哥')
print(fun_bmi.__defaults__)  # 可以看到函数当中设置了什么默认值