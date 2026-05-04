# 练习题1：写一个程序，输入一个数字，判断它是正数、负数还是零

num = float(input('请输入一个数字:'))

if num > 0:
    print('正数')
elif num == 0:
    print('零')
else:
    print('负数')

# 练习题2：打印1到100之间所有能被3整除的数

for i in range(1,101):
    if i % 3 == 0:
        print(i)
    else:
        continue

# 练习题3：给定一个列表 [34, -5, 78, 12, -3, 99]，只打印正数

numbers = [34, -5, 78, 12, -3, 99]

for a in numbers:
    if a > 0:
        print(a)

# 练习题4：计算1到50的所有整数之和（答案是1275，用来验证）

total = 0
for a in range(1,51):
    total += a

print(total)

# 练习题5：写一个猜数字游戏（预设数字=42，用户输入猜测，循环直到猜对）

ans = 42

while True:
    input_num = int(input('请输入一个整数'))
    if input_num < ans:
        print('更大')
    elif input_num > ans:
        print('更小')
    else:
        print('猜对了！')
        break

# 练习题6（金融场景）：给定股价列表，找出最高价、最低价、平均价
prices = [180.5, 195.2, 188.0, 201.3, 175.8, 210.0, 192.5]
