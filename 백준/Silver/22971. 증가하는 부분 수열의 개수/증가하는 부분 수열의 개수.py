N = int(input())
L = list(map(int, input().split()))
memo = [1 for _ in range(N)]
for i in range(1, N):
    for j in range(i, 0, -1):
        if L[j-1] < L[i]:
            memo[i] += memo[j-1]
            memo[i] %= 998244353
print(*memo)