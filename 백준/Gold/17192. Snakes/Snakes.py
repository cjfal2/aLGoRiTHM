import sys
input = sys.stdin.readline

N, K = map(int, input().split())
a = list(map(int, input().split()))

# 누적합
prefix_sum = [0] * (N + 1)
for i in range(N):
    prefix_sum[i+1] = prefix_sum[i] + a[i]

# waste[i][j] = i~j까지 고정 net size로 했을 때 낭비 공간
waste = [[0] * N for _ in range(N)]
for i in range(N):
    max_val = a[i]
    for j in range(i, N):
        max_val = max(max_val, a[j])
        total = prefix_sum[j+1] - prefix_sum[i]
        waste[i][j] = max_val * (j - i + 1) - total

# dp[i][k] = i번째 그룹까지, k번 size 변경했을 때 최소 낭비
dp = [[float('inf')] * (K + 1) for _ in range(N)]

# 초기값 (0번 size 변경 = 처음부터 한 net size로만 처리)
for i in range(N):
    dp[i][0] = waste[0][i]

# DP 채우기
for k in range(1, K + 1):
    for i in range(N):
        for j in range(i):
            dp[i][k] = min(dp[i][k], dp[j][k - 1] + waste[j + 1][i])

print(min(dp[N - 1]))
