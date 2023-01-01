import sys
input = sys.stdin.readline

N = int(input().strip())

dp = [0 for _ in range(N+1)]
be = [0 for _ in range(N+1)]
be[1] = 1

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    be[i] = i - 1
    if not i%3 and dp[i] > dp[i//3] + 1:
        dp[i] = dp[i//3] + 1
        be[i] = i // 3
    if not i%2 and dp[i] > dp[i//2] + 1:
        dp[i] = dp[i//2] + 1
        be[i] = i // 2

A = N
a = []
while A != 1:
    A = be[A]
    a.append(A)
print(dp[N])
print(N, *a)
