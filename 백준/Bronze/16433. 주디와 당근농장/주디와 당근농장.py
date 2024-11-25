N, R, C = map(int, input().split())
R -= 1
C -= 1
pan = [['.' for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if (i + j) % 2 == (R + C) % 2:
            pan[i][j] = 'v'

for p in pan:
    print(*p, sep="")