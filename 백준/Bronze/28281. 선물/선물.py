N, M = map(int, input().split())
arr = list(map(int, input().split()))
min_cost = float("INF")
for n in range(N-1):
    min_cost = min(min_cost, (arr[n]+arr[n+1])*M)
print(min_cost)