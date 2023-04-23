import sys
input = sys.stdin.readline


def dfs(cnt):
    if cnt == 81:
        for i in range(9):
            print(*pan[i], sep="")
        quit()

    x = cnt // 9
    y = cnt % 9
    if pan[x][y] == 0:
        for i in range(1, 10):
            if not garo[x][i] and not sero[y][i] and not nemo[(x//3)*3 + (y//3)][i]:
                garo[x][i] = 1
                sero[y][i] = 1
                nemo[(x//3)*3 + (y//3)][i] = 1
                pan[x][y] = i
                dfs(cnt + 1)
                pan[x][y] = 0
                nemo[(x//3)*3 + (y//3)][i] = 0
                sero[y][i] = 0
                garo[x][i] = 0
    else:
        dfs(cnt + 1)


pan = [[0 for _ in range(9)] for _ in range(9)]
garo = [[0 for _ in range(10)] for _ in range(9)]
sero = [[0 for _ in range(10)] for _ in range(9)]
nemo = [[0 for _ in range(10)] for _ in range(9)]

for i in range(9):
    number = input().strip()
    for j in range(len(number)):
        pan[i][j] = int(number[j])
        if pan[i][j] != 0:
            garo[i][pan[i][j]] = 1
            sero[j][pan[i][j]] = 1
            nemo[(i//3)*3 + (j//3)][pan[i][j]] = 1

dfs(0)
