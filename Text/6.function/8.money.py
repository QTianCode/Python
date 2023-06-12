"""
  作者：LCQT
  日期：2023年05月03日09:50
  项目描述：模拟结算金额
"""
def fun_checkout(money):
    '''
    功能：计算商品合计金额并进行折扣处理
    :param money: 保存的商品金额的列表
    :return: 商品的合计金额和折扣后的金额
    '''
    money_old = sum(money)
    money_new = money_old
    if 500 <= money_old < 1000:
        money_new = '{:.2f}'.format(money_old * 0.9) # '{:.2f}'格式化为两位小数
    elif 1000 <= money_old <2000:
        money_new = '{:.2f}'.format(money_old * 0.8) # 八折优惠
    elif 2000 <= money_old < 3000:
        money_new = '{:.2f}'.format(money_old * 0.7) # 七折优惠
    elif 3000 <= money_old :
        money_new = '{:.2f}'.format(money_old * 0.6) # 六折优惠
    return money_old, money_new    # 返回总金额和折扣后的金额
# 调用函数
print('\n开始结算\n')
list_money = []
while True:
    inmoney = float(input('请输入商品金额（输入0表示输入完毕）：'))
    if int(inmoney) == 0:
        break
    else:
        list_money.append(inmoney)
        money = fun_checkout(list_money)
print('合计金额为:', money[0], '\t应付金额为:', money[1])

