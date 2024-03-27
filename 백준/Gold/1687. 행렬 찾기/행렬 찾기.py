n, m = map(int, input().split())

matrix = [[0] * (m + 1) for _ in range(n + 1)]
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    temp = input()
    for j in range(1, m + 1):
        if temp[j - 1] == '0':
            matrix[i][j] = 1
        elif temp[j - 1] == '1':
            matrix[i][j] = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + matrix[i][j]

ans = 0
for i in range(1, m + 1):
    for j in range(i, m + 1):
        cnt = 0
        for k in range(1, n + 1):
            temp = dp[k][j] - dp[k][i - 1] - dp[k - 1][j] + dp[k - 1][i - 1]
            if temp == j - i + 1:
                cnt += temp
                ans = max(ans, cnt)
            else:
                cnt = 0

print(ans)
