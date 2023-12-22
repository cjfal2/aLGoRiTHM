def ox_func(n, ms, me):
    hap = int(pan[n][me]) if me % 2 else int("".join(pan[n][me-1:me+1]))

    if int(pan[n][ms]) + int(pan[n][ms+2]) == hap:
        pan[n][ms-1] = pan[n][me+1] = "*"
        for k in range(ms, me+1):
            pan[n-1][k] = pan[n+1][k] = "*"
    else:
        pan[n-1][ms+2] = pan[n][ms+1] = pan[n+1][ms] = "/"


N, M = map(int, input().split())
pan = [list(input()) for _ in range(N*3)]

for i in range(1, 3*N, 3):
    for j in range(1, 8*M, 8):
        ox_func(i, j, j+4) if pan[i][j+5] == "." else ox_func(i, j, j+5)

    for a in range(i-1, i+2):
        print(*pan[a], sep="")
