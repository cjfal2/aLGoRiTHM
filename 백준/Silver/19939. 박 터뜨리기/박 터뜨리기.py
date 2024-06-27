n, k = map(int, input().split())
n -= sum(range(1, k + 1))
print(-1 if n < 0 else (k if n % k else k-1))