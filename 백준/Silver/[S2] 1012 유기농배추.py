def bfs(i, j):
    q = []
    q.append((i, j))
    visited[i][j] = 1
    while q:
        x, y = q.pop(0)
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = x + di, y + dj
            if 0<=ni<N and 0<=nj<M and pan[ni][nj] == 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[x][y] + 1


for tc in range(int(input())):
    M, N, K = map(int, input().split())
    pan = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        pan[y][x] = 1
    co = 0
    for i in range(N):
        for j in range(M):
            if pan[i][j] == 1 and visited[i][j] == 0:
                bfs(i, j)
                co += 1
    print(co)
