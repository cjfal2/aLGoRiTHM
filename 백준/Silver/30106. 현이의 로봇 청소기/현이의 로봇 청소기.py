N, M, K = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
answer = 0
for n in range(N):
    for m in range(M):
        if not visited[n][m]:
            answer += 1
            visited[n][m] = 1
            q = [(n, m, pan[n][m])]
            while q:
                x, y, num = q.pop(0)
                for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                    nx, ny = x + dx, y + dy
                    if N > nx >= 0 and M > ny >= 0 and not visited[nx][ny] and abs(pan[nx][ny] - num) <= K:
                        visited[nx][ny] = 1
                        q.append((nx, ny, pan[nx][ny]))

print(answer)