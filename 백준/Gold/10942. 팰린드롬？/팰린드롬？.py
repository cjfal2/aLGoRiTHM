import sys
sys.setrecursionlimit(10000000)
IP = sys.stdin.readline


def pal(L):
    N = len(L)
    dp = [[0] * N for _ in range(N)]

    # 길이가 1
    for i in range(N):
        dp[i][i] = 1

    # 길이가 2
    for i in range(N-1):
        if L[i] == L[i+1]:
            dp[i][i+1] = 1

    # 길이가 3 이상
    for length in range(2, N):
        for start in range(N - length):
            end = start + length
            if L[start] == L[end] and dp[start+1][end-1]:
                dp[start][end] = 1

    return dp


N = int(IP().strip())
L = list(map(int, IP().strip().split()))
M = int(IP().strip())

dp = pal(L)

for _ in range(M):
    S, E = map(int, IP().strip().split())
    print(dp[S-1][E-1])
