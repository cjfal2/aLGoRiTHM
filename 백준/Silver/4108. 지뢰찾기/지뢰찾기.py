import sys
input = sys.stdin.readline


def check(x, y):
    num = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if N > i >= 0 and M > j >= 0 and (x, y) != (i, j) and pan[i][j] == "*":
                num += 1
    return num


while 1:
    N, M = map(int, input().strip().split())
    if N == M == 0:
        break
    pan = [list(input().strip()) for _ in range(N)]
    for n in range(N):
        for m in range(M):
            if pan[n][m] == ".":
                pan[n][m] = check(n, m)
    for v in pan:
        print(*v, sep="")