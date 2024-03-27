N, M = map(int, input().split())
matrix = [[0 if x == "1" else 1 for x in input()] for _ in range(N)]
dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = matrix[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

answer = 0
for i in range(1, M + 1):
    for j in range(i, M + 1):
        cnt = 0
        for k in range(1, N + 1):
            temp = dp[k][j] - dp[k][i - 1] - dp[k - 1][j] + dp[k - 1][i - 1]
            if temp == j - i + 1:
                cnt += temp
                answer = max(answer, cnt)
            else:
                cnt = 0
print(answer)
