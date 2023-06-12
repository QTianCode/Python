"""
  作者：LCQT
  日期：2023年06月06日00:03
  项目描述：通过输入的菜品和价格输出特定的菜单
"""
# 菜单生成器
print("输入菜单的菜品,价格的格式如：红烧肉，28")
menu1 = input("请输入菜品、价格：")
menu2 = input("请输入菜品、价格：")
menu3 = input("请输入菜品、价格：")
ind1 = tuple(menu1.split("，"))
ind2 = tuple(menu2.split("，"))
ind3 = tuple(menu3.split("，"))
print("".center(27, '-'))
# chr(12288) 处理中文填充一致问题
# chr(12288) 是中文空格的编码，采用中文空格是因为输入的中文不一定相同长度，如果用西文空格来填补会导致实际字符宽度不一致。
print("|{: ^10}\t{: ^8} |".format("菜品", "价格", chr(12288)))    # chr 的作用
print("|{: ^10}\t{: ^10}|".format(ind1[0], ind1[1], chr(12288)))
print("|{: ^10}\t{: ^10}|".format(ind2[0], ind2[1], chr(12288)))
print("|{: ^10}\t{: ^10}|".format(ind3[0], ind3[1], chr(12288)))
print("|{: ^10}\t{: ^10}|".format("总价", int(ind1[1]) + int(ind2[1]) + int(ind3[1]), chr(12288)))
print("".center(27, '-'))
