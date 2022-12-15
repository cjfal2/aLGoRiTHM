def bfs(i, j):
    global co
    co += 1
    visited[i][j] = 1
    q = [(i, j)]
    while q:
        x, y = q.pop(0)
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx, ny = x + dx, y + dy
            if N > nx >= 0 and M > ny >= 0 and not visited[nx][ny] and sheep[nx][ny] == "#":
                visited[nx][ny] = 1
                q.append((nx, ny))


for _ in range(int(input())):
    N, M = map(int, input().split())
    sheep = [list(input()) for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    co = 0
    for n in range(N):
        for m in range(M):
            if not visited[n][m] and sheep[n][m] == "#":
                bfs(n, m)
    print(co)
                        