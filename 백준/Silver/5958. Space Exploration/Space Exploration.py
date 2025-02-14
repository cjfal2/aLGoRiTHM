N = int(input())
answer = 0
pan = [input() for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if pan[i][j] == "*" and not visited[i][j]:
            visited[i][j] = 1
            answer += 1
            q = [(i, j)]
            while q:
                x, y = q.pop(0)
                for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                    nx, ny = x + dx, y + dy
                    if N > nx >= 0 and N > ny >= 0 and not visited[nx][ny] and pan[nx][ny] == "*":
                        q.append((nx, ny))
                        visited[nx][ny] = 1
print(answer)