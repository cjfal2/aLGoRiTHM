num1 = 0
num2 = 0
max_num = 0
while 1:
    try:
        n, m = map(int, input().split())
        num2 -= n
        num2 += m
        max_num = max(num2, max_num)
        num1 = num2
    except:
        print(max_num)
        break