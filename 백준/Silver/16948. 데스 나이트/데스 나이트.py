N = int(input())
pan = [[0 for _ in range(N)] for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
sx, sy, ex, ey = map(int, input().split())
visited[sx][sy] = 1
q = [(sx, sy)]
while q:
    x, y = q.pop(0)
    if x == ex and y == ey:
        print(visited[x][y]-1)
        quit()
    for dx, dy in (-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1):
        nx, ny = x + dx, y + dy
        if N > nx >= 0 and N > ny >= 0 and not visited[nx][ny]:
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))
print(-1)