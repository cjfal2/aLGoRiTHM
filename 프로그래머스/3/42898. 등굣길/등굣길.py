def solution(M, N, puddles):

    pan = [[1 for _ in range(M)] for _ in range(N)]
    mod = 1000000007

    for m, n in puddles:
        if m == 1:
            for i in range(n-1, N):
                pan[i][m-1] = 0
        if n == 1:
            for i in range(m-1, M):
                pan[n-1][i] = 0

    for m, n in puddles:
        pan[n-1][m-1] = 0

    for n in range(N):
        for m in range(M):
            if m-1 < 0 or n-1 < 0:
                continue
            if pan[n][m] == 0:
                continue
            pan[n][m] = (pan[n][m-1] + pan[n-1][m]) % mod

    return pan[N-1][M-1] % mod