N, M = map(int, input().split())
pan = [[0 for _ in range(M)] for _ in range(N)]
i = 0
for n in range(N):
    for m in range(M):
        i += 1
        pan[n][m] = i
for p in pan:
    print(*p)