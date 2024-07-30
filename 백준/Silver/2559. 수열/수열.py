N, K = map(int, input().split())
numbers = list(map(int, input().split()))
prefix_sum = [0]
for i in range(N):
    prefix_sum.append(numbers[i]+prefix_sum[i])
answer = -float("INF")
for i in range(K, N+1):
    new_sum = prefix_sum[i] - prefix_sum[i-K]
    answer = max(answer, new_sum)
print(answer)