def bfs():
    visited = [[0 for _ in range(M)] for _ in range(N)]
    for n in range(N):
        for m in range(M):
            if not visited[n][m]:
                visited[n][m] = 1
                what = pan1[n][m]
                change = pan2[n][m]
                pan1[n][m] = change
                q = [(n, m)]
                while q:
                    x, y = q.pop(0)
                    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                        nx, ny = x + dx, y + dy
                        if N > nx >= 0 and M > ny >= 0 and pan1[nx][ny] == what and visited[nx][ny] == 0:
                            visited[nx][ny] = 1
                            pan1[nx][ny] = change
                            q.append((nx, ny))


N, M = map(int, input().split())
pan1 = [list(input()) for _ in range(N)]
pan2 = [list(input()) for _ in range(N)]

bfs()
print("YES" if pan1 == pan2 else "NO")
