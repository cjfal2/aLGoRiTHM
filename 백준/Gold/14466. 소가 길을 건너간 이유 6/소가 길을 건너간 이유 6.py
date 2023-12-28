from collections import deque


def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nx, ny = x + dx, y + dy
            if N >= nx > 0 and N >= ny > 0 and not visited[nx][ny] and not roads[x][y][nx][ny] and not roads[nx][ny][x][y]:
                visited[nx][ny] = 1
                q.append((nx, ny))


N, K, R = map(int, input().split())
roads = [[[ [0 for _ in range(N+1)] for _ in range(N+1)] for _ in range(N+1)] for _ in range(N+1)]
visited = [[0 for _ in range(N+1)] for _ in range(N+1)]
cows = []

for _ in range(R):
    r1, c1, r2, c2 = map(int, input().split())
    roads[r1][c1][r2][c2] = 1

for _ in range(K):
    a, b = map(int, input().split())
    cows.append((a, b))

cnt = 0
for i in range(K):
    visited = [[0 for _ in range(N+1)] for _ in range(N+1)]
    bfs(cows[i][0], cows[i][1])
    for j in range(i + 1, K):
        if not visited[cows[j][0]][cows[j][1]]:
            cnt += 1

print(cnt)

