def can_go(i, j, v):
    if i < 0 or i >= N:
        return False
    
    if j < 0 or j >= M:
        return False
    
    if v[i][j]:
        return False
    
    if pan[i][j]:
        return False
    
    for a in range(i, i + A):
        for b in range(j, j + B):
            if a < 0 or a >= N:
                return False
    
            if b < 0 or b >= M:
                return False
            
            if pan[a][b]:
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
        if can_go(nx, ny, visited):
            q.append((nx, ny, cnt+1))
            visited[nx][ny] = 1
print(-1)
