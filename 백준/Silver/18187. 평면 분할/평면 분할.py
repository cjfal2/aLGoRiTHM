n = int(input())

dp = [0 for _ in range(101)]
dp[1] = 2
dp[2] = 4

temp = 3
for i in range(3, n+1):
    dp[i] = dp[i-1]+temp
    if i % 3 != 0:
        temp += 1

print(dp[n])
