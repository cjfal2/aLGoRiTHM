N, M = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1 for _ in range(M)] for _ in range(N)]


def dfs(x, y, num):
    if x == N - 1 and y == M - 1:
        return 1

    if visited[x][y] != -1:
        return visited[x][y]

    roads = 0
    for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
        nx, ny = x + dx, y + dy
        if N > nx >= 0 and M > ny >= 0 and num > pan[nx][ny]:
            roads += dfs(nx, ny, pan[nx][ny])

    visited[x][y] = roads
    return visited[x][y]

dfs(0, 0, pan[0][0])

print(visited[0][0])