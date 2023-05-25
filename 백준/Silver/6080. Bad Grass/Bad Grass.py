import sys
input = sys.stdin.readline


def bfs(i, j):
    visited[i][j] = 1
    q = [(i, j)]
    while q:
        x, y = q.pop(0)
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]:
            nx, ny = x + dx, y + dy
            if N > nx >= 0 and M > ny >= 0 and not visited[nx][ny] and san[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny))


N, M = map(int, input().strip().split())
san = [list(map(int, input().strip().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
co = 0
for n in range(N):
    for m in range(M):
        if not visited[n][m] and san[n][m]:
            bfs(n, m)
            co += 1
print(co)
