import sys
input = sys.stdin.readline

D, N = map(int, input().split())

# 날씨 데이터
T = [int(input().strip()) for _ in range(D)]

# 옷 데이터 (최소 온도, 최대 온도, 화려함)
clothes = [tuple(map(int, input().split())) for _ in range(N)]

# DP 테이블 초기화
dp = [[-1] * N for _ in range(D)]

# 각 날짜별 입을 수 있는 옷 미리 저장
valid_clothes = [[] for _ in range(D)]

for j in range(N):
    Aj, Bj, Cj = clothes[j]
    for i in range(D):
        if Aj <= T[i] <= Bj:
            valid_clothes[i].append(j)

# 첫째 날 초기화
for j in valid_clothes[0]:
    dp[0][j] = 0  # 첫날은 차이가 없음

# DP 수행
for i in range(1, D):  # 1일부터 D-1일까지
    for j in valid_clothes[i]:  # i일에 입을 수 있는 옷
        Aj, Bj, Cj = clothes[j]

        max_diff = 0
        for k in valid_clothes[i-1]:  # (i-1)일에 입을 수 있는 옷
            Ak, Bk, Ck = clothes[k]
            max_diff = max(max_diff, dp[i-1][k] + abs(Cj - Ck))

        dp[i][j] = max_diff  # i일에 j번 옷을 입을 때 최대값 갱신

# 마지막 날에서 최대값 출력
print(max(dp[D-1]))
