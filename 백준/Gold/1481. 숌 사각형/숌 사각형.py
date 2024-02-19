def solution(idx):
    global flag

    if idx >= N * N:
        for i in range(N):
            if i > diff and (not garo[i][0] or not sero[i][0]):
                flag = False
                return
            for k in range(1, D):
                if not garo[i][k] or not sero[i][k]:
                    flag = False
                    return
        flag = True
        return

    x = idx // N
    y = idx % N
    if diff < x and diff < y:
        for k in range(D):
            if garo[x][k] or sero[y][k]:
                continue

            pan[x][y] = k
            garo[x][k] = sero[y][k] = True

            if y == N - 1:
                solution(idx + diff + 2)
            else:
                solution(idx + 1)
            if flag:
                return

            pan[x][y] = 0
            garo[x][k] = sero[y][k] = False


N, D = map(int, input().split())
pan = [[0 for _ in range(N)] for _ in range(N)]
garo = [[False for _ in range(D)] for _ in range(N)]
sero = [[False for _ in range(D)] for _ in range(N)]
diff = N - D
flag = False

for i in range(diff + 1):
    for j in range(1, D):
        pan[i][diff + j] = j
        garo[i][j] = True
        sero[diff + j][j] = True

for j in range(diff + 1):
    for i in range(1, D):
        pan[diff + i][j] = i
        sero[j][i] = True
        garo[diff + i][i] = True

solution(N * (diff + 1) + diff + 1)

for p in pan:
    print(*p)
