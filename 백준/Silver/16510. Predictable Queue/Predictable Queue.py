import bisect
import sys
input = sys.stdin.readline


N, M = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))

# 누적 합 계산
prefix_sum = [0 for _ in range(N+1)]
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

for _ in range(M):
    print(bisect.bisect_right(prefix_sum, int(input().strip())) - 1)