def check(i, j):
    for a in range(i, i + A):
        for b in range(j, j + B):
            if a < 0 or a >= N or b < 0 or b >= M or pan[a][b]:
                return False
    return True


N, M, A, B, K = map(int, input().split())
pan = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(K):
    a, b = map(lambda x: int(x)-1, input().split())
    pan[a][b] = 1

sx, sy = map(lambda x: int(x)-1, input().split())
ex, ey = map(lambda x: int(x)-1, input().split())
q = [(sx, sy, 0)]
visited = [[0 for _ in range(M)] for _ in range(N)]
visited[sx][sy] = 1
while q:
    x, y, cnt = q.pop(0)
    if (x, y) == (ex, ey):
        print(cnt)
        quit()
    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
        nx, ny = x + dx, y + dy
        if N > nx >= 0 and M > ny >= 0 and not visited[nx][ny] and not pan[nx][ny]:
            if check(nx, ny):
                q.append((nx, ny, cnt+1))
                visited[nx][ny] = 1
print(-1)
