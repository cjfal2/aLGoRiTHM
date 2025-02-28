import sys

# 입력 받기
R, S = map(int, sys.stdin.readline().split())
grid = [list(sys.stdin.readline().strip()) for _ in range(R)]

# 유성과 땅의 위치 찾기
meteor_bottom = {}  # 각 열에서 유성의 가장 아래 위치
ground_top = {}  # 각 열에서 땅의 가장 위 위치

for j in range(S):
    meteor_bottom[j] = -1
    ground_top[j] = R  # 초기값: 땅이 없을 경우 최하단

for i in range(R):
    for j in range(S):
        if grid[i][j] == 'X':
            meteor_bottom[j] = max(meteor_bottom[j], i)
        elif grid[i][j] == '#':
            ground_top[j] = min(ground_top[j], i)

# 유성이 떨어질 수 있는 거리 계산
fall_distance = R  # 최대로 떨어질 수 있는 거리
for j in range(S):
    if meteor_bottom[j] != -1:  # 유성이 있는 열만 계산
        fall_distance = min(fall_distance, ground_top[j] - meteor_bottom[j] - 1)

# 새로운 격자 생성
new_grid = [['.'] * S for _ in range(R)]

# 기존 땅을 그대로 배치
for i in range(R):
    for j in range(S):
        if grid[i][j] == '#':
            new_grid[i][j] = '#'

# 유성을 새로운 위치로 이동
for i in range(R):
    for j in range(S):
        if grid[i][j] == 'X':
            new_grid[i + fall_distance][j] = 'X'

# 결과 출력
for row in new_grid:
    print("".join(row))
