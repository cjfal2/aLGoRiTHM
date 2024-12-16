def check(x, y, num):
    res = 0
    
    # up
    for i in range(x):
        if pan[i][y] >= num:
            break
    else:
        res += 1

    # down
    for i in range(x+1, N):
        if pan[i][y] >= num:
            break
    else:
        res += 1

    # left
    for j in range(y):
        if pan[x][j] >= num:
            break
    else:
        res += 1

    # right
    for j in range(y+1, M):
        if pan[x][j] >= num:
            break
    else:
        res += 1
    return res


N, M = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(N)]

answer = 0
for n in range(N):
    for m in range(M):
        answer += check(n, m, pan[n][m])
print(answer)