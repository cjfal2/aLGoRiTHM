N = int(input())
memo = [0, 1, 1] + [0 for _ in range(N)]
for i in range(3, N+1):
    memo[i] = (memo[i - 1] + memo[i - 2]) % 1000000007
print(memo[N])