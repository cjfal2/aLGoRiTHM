from collections import deque

pan = [list(map(int, input().split())) for _ in range(5)]
n, m = map(int, input().split())
visited = [[0 for _ in range(5)] for _ in range(5)]
visited[n][m] = 1
q = deque()
q.append((n, m))
while q:
    x, y = q.popleft()
    for dx, dy in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
        nx, ny = x + dx, y + dy
        if 5 > nx >= 0 and 5 > ny >= 0 and not visited[nx][ny]:
            if pan[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
            elif pan[nx][ny] == 1:
                print(visited[x][y])
                quit()
print(-1)
