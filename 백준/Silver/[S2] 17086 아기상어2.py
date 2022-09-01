def bfs(i, j, v, w):
    visited = [[0 for _ in range(w)] for _ in range(v)]
    q = []
    q.append((i, j))
    visited[i][j] = 1
    while q:
        x, y = q.pop(0)
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]:
            ni, nj = x + di, y + dj
            if 0<=ni<v and 0<=nj<w and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[x][y] + 1
                if shark[ni][nj] == 1:
                    # for K in visited:
                    #     print(K)
                    # print("##############")
                    return int(visited[ni][nj])-1
    return 100000

N, M = map(int, input().split())
shark = [list(map(int, input().split())) for _ in range(N)]

co = []
for i in range(N):
    for j in range(M):
        if shark[i][j] == 0:
            a = bfs(i,j,N,M)
            co.append(a)
print(max(co))
