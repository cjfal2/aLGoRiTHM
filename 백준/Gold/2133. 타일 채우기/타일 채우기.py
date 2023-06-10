N = int(input())
if N % 2:
    print(0)
    quit()

dp = [0 for _ in range(N+1)]
dp[0] = 1
dp[2] = 3

for n in range(3, N+1):
    for i in range(2, N+1, 2):
        if i == 2:
            dp[n] = dp[n-i] * dp[2]
        elif n-i >= 0:
            dp[n] += dp[n-i] * 2

print(dp[N])
