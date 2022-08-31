def bfs(i, j, N, M):
    visited = [[0 for _ in range(M)] for _ in range(N)]
    q = []
    q.append((i, j))
    visited[i][j] = 1
    while q:
        i, j = q.pop(0)
        if i == N-1 and j == M-1:
            return visited[N-1][M-1]
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0<=ni<N and 0<=nj<M and maze[ni][nj] != 0 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1


N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
print(bfs(0, 0, N, M))
