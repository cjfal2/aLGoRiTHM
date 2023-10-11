N, M = map(int, input().split())
pan = [input() for _ in range(N)]
answer = -1
visited = [[0 for _ in range(M)] for _ in range(N)]
for n in range(N):
    for m in range(M):
        if pan[n][m] == "." and not visited[n][m]:
            visited[n][m] = 1
            q = [(n, m)]
            rooms = 1
            while q:
                x, y = q.pop(0)
                for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                    nx, ny = x + dx, y + dy
                    if N > nx >= 0 and M > ny >= 0 and not visited[nx][ny] and pan[nx][ny] == ".":
                        q.append((nx, ny))
                        visited[nx][ny] = 1
                        rooms += 1
            answer = max(answer, rooms)
print(answer)
                        