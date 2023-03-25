def bfs(i, j, what):
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[i][j] = 1
    memory = before[i][j]
    before[i][j] = what
    q = [(i, j)]
    while q:
        x, y = q.pop(0)
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nx, ny = x + dx, y + dy

            if N > nx >= 0 and M > ny >= 0 and before[nx][ny] == memory and not visited[nx][ny]:
                visited[nx][ny] = True
                before[nx][ny] = what
                q.append((nx, ny))


N, M = map(int, input().split())
before = [list(map(int, input().split())) for _ in range(N)]
after = [list(map(int, input().split())) for _ in range(N)]

check = 1
for n in range(N):
    for m in range(M):
        if before[n][m] != after[n][m]:
            bfs(n, m, after[n][m])
            check = 0
            break
    if not check:
        break

for n in range(N):
    for m in range(M):
        if before[n][m] != after[n][m]:
            print("NO")
            quit()

print('YES')