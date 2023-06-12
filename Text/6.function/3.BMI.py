"""
  作者：LCQT
  日期：2023年05月02日18:47
  项目描述：计算BMI
"""
def fun_bmi(person, height, weight):
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

# 调用函数
while True:
    name = str(input('请输入姓名：'))
    if name == '结束':
        break
    height = float(input('请输入身高（单位：米）：'))
    weight = float(input('请输入体重（单位：KG）：'))
    fun_bmi(name, height, weight)
