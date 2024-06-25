import sys
input = sys.stdin.readline


for _ in range(int(input())):
    N = int(input())
    L = [list(map(int, input().split())) for _ in range(2)]

    dp = [[0 for _ in range(N)] for _ in range(2)]
    dp[0][0] = L[0][0]
    dp[1][0] = L[1][0]
    if N == 1:
        print(max(dp[0][0], dp[1][0]))
    else:
        dp[0][1] = L[1][0] + L[0][1]
        dp[1][1] = L[0][0] + L[1][1]
        if N == 2:
            print(max(dp[0][1], dp[1][1]))
        else:
            for i in range(2, N):
                dp[0][i] = max(dp[1][i - 2], dp[1][i - 1]) + L[0][i]
                dp[1][i] = max(dp[0][i - 2], dp[0][i - 1]) + L[1][i]

            print(max(dp[0][-1], dp[1][-1]))
