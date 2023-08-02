X, Y, N = map(int, input().split())
X+=500
Y+=500
pan = [[0 for _ in range(1001)] for _ in range(1001)]
for _ in range(N):
    a, b = map(lambda x: int(x) + 500, input().split())
    pan[a][b] = 1

visited = [[0 for _ in range(1001)] for _ in range(1001)]
visited[500][500] = 1
q = [(500, 500)]
while q:
    x, y = q.pop(0)
    if x == X and y == Y:
        print(visited[x][y] - 1)
        break
    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
        nx, ny = x + dx, y + dy
        if 1000 >= nx >= 0 and 1000 >= ny >= 0 and not pan[nx][ny] and not visited[nx][ny]:
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))
        
