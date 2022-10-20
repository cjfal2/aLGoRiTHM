def bfs(xx, yy, color):
    global pan
    pan[xx][yy] = 0
    q = [(xx, yy)]
    co = 1
    while q:
        x, y = q.pop(0)
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx, ny = x + dx, y + dy
            if M > nx >= 0 and N > ny >= 0 and pan[nx][ny] == color:
                pan[nx][ny] = 0
                q.append((nx, ny))
                co += 1
    return co ** 2


N, M = map(int, input().split())
pan = [list(input()) for _ in range(M)]
w = 0
b = 0
for m in range(M):
    for n in range(N):
        if pan[m][n] == 'W':
            w += bfs(m, n, 'W')
        elif pan[m][n] == 'B':
            b += bfs(m, n, 'B')
print(w, b)