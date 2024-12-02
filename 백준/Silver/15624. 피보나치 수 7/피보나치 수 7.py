N = int(input())
memo = [1, 1] + [0 for _ in range(N)]
for i in range(2, N):
    memo[i] = (memo[i - 1] + memo[i - 2]) % 1000000007
print(memo[N - 1])