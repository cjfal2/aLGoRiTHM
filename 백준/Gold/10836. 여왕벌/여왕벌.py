import sys
input = sys.stdin.readline

M, N = map(int, input().split())

# 각 칸의 성장을 나타내는 리스트를 0으로 초기화
growth = [0] * (2 * M - 1)

# 입력을 받아 성장 정보를 누적
for _ in range(N):
    zero, one, two = map(int, input().split())
    idx = 0
    for _ in range(zero):
        growth[idx] += 0
        idx += 1
    for _ in range(one):
        growth[idx] += 1
        idx += 1
    for _ in range(two):
        growth[idx] += 2
        idx += 1

# 벌집 초기화
hive = [[1] * M for _ in range(M)]

# 가장자리 성장 적용
index = 0
for i in range(M-1, -1, -1):
    hive[i][0] += growth[index]
    index += 1
for j in range(1, M):
    hive[0][j] += growth[index]
    index += 1

# 내부 애벌레 성장 적용
for i in range(1, M):
    for j in range(1, M):
        hive[i][j] = max(hive[i-1][j], hive[i][j-1], hive[i-1][j-1])

# 결과 출력
for row in hive:
    print(*row)
