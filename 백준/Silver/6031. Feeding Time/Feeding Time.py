M, N = map(int, input().split())
pan = [input() for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
answer = 0
for n in range(N):
    for m in range(M):
        if pan[n][m] == ".":
            visited[n][m] = 1
            q = [(n, m)]
            temp = 1
            while q:
                x, y = q.pop(0)
                for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1):
                    nx, ny = x + dx, y + dy
                    if N > nx >= 0 and M > ny >= 0 and pan[nx][ny] == "." and not visited[nx][ny]:
                        visited[nx][ny] = 1
                        q.append((nx, ny))
                        temp += 1
            answer = max(answer, temp)
print(answer)