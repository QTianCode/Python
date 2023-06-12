# 开发者 : 晴天
# 开发日期 : 2023/4/23
# 列表推导式
print('生成1到10之间偶数的平方')
list1 = [i*i for i in range(2, 11, 2)]
print(list1)

price = [1000, 500, 800, 888, 666]
sale = [int(x * 0.5) for x in price]
print('原价格', price)
print('打五折后的价格', sale)
big = [x for x in price if x > 800]
print('大于800元的价格有:', big)
