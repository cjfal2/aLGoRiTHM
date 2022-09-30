while 1:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    visited = [[0 for _ in range(w)] for _ in range(h)]
    dokdo = [list(map(int, input().split())) for _ in range(h)]
    co = 0
    for i in range(h):
        for j in range(w):
            if dokdo[i][j] == 1 and visited[i][j] == 0:
                q = []
                visited[i][j] = 1
                q.append([i, j])
                co += 1
                while q:
                    tx, ty = q.pop(0)
                    for dx, dy in [[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]:
                        nx = tx + dx
                        ny = ty + dy
                        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and dokdo[nx][ny]:
                            visited[nx][ny] = 1
                            q.append([nx, ny])
    print(co)