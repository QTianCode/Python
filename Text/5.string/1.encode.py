# 开发者 : 晴天
# 开发日期 : 2023/4/25
# 编码转换
str1 = '遗憾才是人生常态'
byte1 = str1.encode('GBK')  # 一个中文占两个字节
byte2 = str1.encode('UTF-8')  # 一个中文占三个字节
print('原字符:', str1)
print('转换GBK后:', byte1)
print('转换UTF-8后:', byte2)

newstr1 = byte1.decode('GBK')
newstr2 = byte2.decode('UTF-8')
print('GBK逆转换后:', newstr1)
print('UTF-8逆转换后:', newstr2)
