N, M = map(int, input().split())
pan = []
for n in range(N):
    a = input()
    for m in range(M):
        if a[m] == "B":
            ex, ey = n, m
        elif a[m] == "C":
            sx, sy = n, m
    pan.append(a)
visited = [[0 for _ in range(M)] for _ in range(N)]
visited[sx][sy] = 1
q = [(sx, sy)]
while q:
    x, y = q.pop(0)
    for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
        nx, ny = x + dx, y + dy
        if N > nx >= 0 and M > ny >= 0 and not visited[nx][ny] and pan[nx][ny] != "*":
            if (nx, ny) == (ex, ey):
                print(visited[x][y])
                quit()
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))