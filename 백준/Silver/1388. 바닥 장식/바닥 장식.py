def bfs(h, w, what):
    global visited, co
    if what == "-":
        dix = [[0, 1], [0, -1]]
    else:
        dix = [[1, 0], [-1, 0]]
    visited[h][w] = True
    q = [(h, w)]
    while q:
        x, y = q.pop(0)
        for dx, dy in dix:
            nx, ny = x + dx, y + dy
            if N > nx >= 0 and M > ny >= 0 and not visited[nx][ny] and pan[nx][ny] == what:
                q.append((nx, ny))
                visited[nx][ny] = True
    co += 1

N, M = map(int, input().split())
pan = [list(input()) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
co = 0
for n in range(N):
    for m in range(M):
        if not visited[n][m]:
            bfs(n, m, pan[n][m])
print(co)