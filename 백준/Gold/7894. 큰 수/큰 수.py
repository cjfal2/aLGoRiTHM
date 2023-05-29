import math


def cal(num):
    temp = math.log10(num)
    for i in range(num-1, 0, -1):
        temp += math.log10(i)
    return int(temp) + 1


for _ in range(int(input())):
    print(cal(int(input())))
