N = int(input())
arr = list(map(int, input().split()))

# 2차월 dp 배열
dp = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N-1):
    if arr[i] != arr[i+1]:
        dp[i][i+1] = 1

for length in range(3, N+1):
    for i in range(N-length+1):
        j = i + length - 1
        if arr[i] == arr[j]:
            dp[i][j] = dp[i+1][j-1]
        else:
            dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1

print(dp[0][N-1])