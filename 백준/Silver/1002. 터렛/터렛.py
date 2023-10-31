import math


for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2)  # 원의 방정식
    a = 0
    if d == 0 and r1 == r2:
        a = -1
    elif abs(r1-r2) == d or r1+r2 == d:
        a = 1
    elif abs(r1-r2) < d < (r1+r2):
        a = 2
    print(a)
