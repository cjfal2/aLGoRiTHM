from math import sqrt


N = int(input())
pan = []
for n in range(N):
    temp = list(map(int, input().split()))
    pan.append(temp)
    for m in range(N):
        if temp[m] == 5:
            px, py = n, m
        elif temp[m] == 2:
            qx, qy = n, m

if sqrt((px-qx)**2 + (py-qy)**2) < 5:
    print(0)
    quit()

sx, sy, ex, ey = min(qx, px), min(qy, py), max(qx, px), max(qy, py)

answer = 0
for n in range(sx, ex+1):
    for m in range(sy, ey+1):
        if pan[n][m] == 1:
            answer += 1
print(1 if answer >= 3 else 0)