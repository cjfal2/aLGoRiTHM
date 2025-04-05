from collections import deque

# 맵 크기
SIZE = 501

# 입력 받기
danger_map = [[0] * SIZE for _ in range(SIZE)]

# 위험 구역: 1
N = int(input())
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(min(x1,x2), max(x1,x2)+1):
        for y in range(min(y1,y2), max(y1,y2)+1):
            if danger_map[x][y] == 0:
                danger_map[x][y] = 1

# 죽음 구역: -1 (최우선)
M = int(input())
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(min(x1,x2), max(x1,x2)+1):
        for y in range(min(y1,y2), max(y1,y2)+1):
            danger_map[x][y] = -1

# BFS (0-1 BFS)
dq = deque()
dq.append((0, 0))
visited = [[-1]*SIZE for _ in range(SIZE)]
visited[0][0] = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while dq:
    x, y = dq.popleft()

    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]

        if 0 <= nx < SIZE and 0 <= ny < SIZE:
            if danger_map[nx][ny] == -1:
                continue  # 죽음의 구역

            cost = danger_map[nx][ny]
            if visited[nx][ny] == -1 or visited[nx][ny] > visited[x][y] + cost:
                visited[nx][ny] = visited[x][y] + cost
                if cost == 0:
                    dq.appendleft((nx, ny))  # 안전 구역
                else:
                    dq.append((nx, ny))      # 위험 구역

# 결과
print(visited[500][500])
