import sys

input = sys.stdin.readline

# 입력 받기
m, n = map(int, input().split())
table = [[0] * (n + 1)] + [[0] + list(map(int, input().split())) for _ in range(m)]

# 누적 합 배열 sum[i][j] 계산
sum_table = [[0] * (n + 1) for _ in range(m + 1)]

for i in range(1, m + 1):
    for j in range(1, n + 1):
        sum_table[i][j] = (
            sum_table[i - 1][j] + sum_table[i][j - 1]
            - sum_table[i - 1][j - 1] + table[i][j]
        )

# 직사각형 합이 10인 경우 찾기
ans = 0

def func(x, y):
    global ans
    for i in range(x, m + 1):
        for j in range(y, n + 1):
            # x행 y열부터 i행 j열까지의 합 계산
            tmp = (
                sum_table[i][j] - sum_table[i][y - 1]
                - sum_table[x - 1][j] + sum_table[x - 1][y - 1]
            )
            if tmp >= 10:
                if tmp == 10:
                    ans += 1
                break  # 불필요한 탐색을 줄이기 위해 종료

# 모든 시작 위치에서 탐색
for i in range(1, m + 1):
    for j in range(1, n + 1):
        func(i, j)

# 결과 출력
print(ans)
