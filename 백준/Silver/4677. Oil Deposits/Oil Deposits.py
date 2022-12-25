while 1:
    N, M = map(int, input().split())
    if N == M == 0:
        quit()
    pan = [list(input()) for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    co = 0
    for n in range(N):
        for m in range(M):
            if not visited[n][m] and pan[n][m] == '@':
                visited[n][m] = 1
                q = [(n, m)]
                while q:
                    x, y = q.pop(0)
                    for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]:
                        nx, ny = x + dx, y + dy
                        if N > nx >= 0 and M > ny >= 0 and not visited[nx][ny] and pan[nx][ny] == '@':
                            q.append((nx, ny))
                            visited[nx][ny] = 1
                co += 1
    print(co)