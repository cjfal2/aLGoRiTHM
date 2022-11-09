def bfs(i, j):
    global top
    visited[i][j] = 1
    q = [(i, j)]
    while q:
        x, y = q.pop(0)
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]:
            nx, ny = x + dx, y + dy
            if N > nx >= 0 and M > ny >= 0:
                if san[nx][ny] > san[x][y]:
                    top = False
                if not visited[nx][ny] and san[nx][ny] == san[x][y]:
                    visited[nx][ny] = 1
                    q.append((nx, ny))


N, M = map(int, input().split())
san = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
co = 0
for n in range(N):
    for m in range(M):
        if san[n][m] and not visited[n][m]:
            top = True
            bfs(n, m)
            if top:
                co += 1
            # print(n, m, co)
            # for v in visited:
            #     print(v)
            # print("---------------------")
print(co)
                        