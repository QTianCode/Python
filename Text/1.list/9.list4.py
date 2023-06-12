# 开发者 : 晴天
# 开发日期 : 2023/4/23
# 列表排序
char = ["cat", 'dog', 'pet', 'TOM']
score = [100, 20, 39, 98, 67, 84, 45]
print("原列表", score)
score.sort()
print("升序", score)
score.sort(reverse=True)
print("降序", score)
char.sort()
print("升序",char)
char.sort(key=str.lower)  # 不区分大小写排序
print("升序",char)

fruit = ["apple",'banana', 'Orange', 'tomato']
print('原列表', fruit)
list = sorted(fruit)
print('升序',list)
list2 = sorted(fruit,reverse=True)
print('降序', list2)
print('原列表', fruit)