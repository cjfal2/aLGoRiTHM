import sys
import math

def min_square_sum(N):
    dp = [float('inf')] * (N + 1)
    dp[0] = 0

    for i in range(1, N + 1):
        for j in range(1, int(math.sqrt(i)) + 1):
            dp[i] = min(dp[i], dp[i - j * j] + 1)

    return dp[N]

N = int(sys.stdin.readline().strip())
print(min_square_sum(N))
