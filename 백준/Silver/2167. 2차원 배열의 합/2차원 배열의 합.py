N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
pan = [[0 for _ in range(M+1)] for _ in range(N+1)]

for n in range(1, N+1):
    for m in range(1, M+1):
        pan[n][m] = arr[n-1][m-1] + pan[n][m-1] + pan[n-1][m] - pan[n-1][m-1]

for _ in range(int(input())):
    sx, sy, ex, ey = map(int, input().split())
    print(pan[ex][ey] - pan[ex][sy-1] - pan[sx-1][ey] + pan[sx-1][sy-1])
