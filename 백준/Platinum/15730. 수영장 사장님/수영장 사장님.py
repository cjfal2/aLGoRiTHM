from collections import deque


N, M = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(N)]

answer = 0
for h in range(1, 10001):
    visited = [[0 for _ in range(M + 2)] for _ in range(N + 2)]

    for i in range(N):
        for j in range(M):
            visited[i + 1][j + 1] = 0 if pan[i][j] < h else 1

    q = deque([(0, 0)])
    visited[0][0] = 1

    while q:
        x, y = q.popleft()
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nx, ny = x + dx, y + dy
            if N+2 > nx >= 0 and M+2 > ny >= 0 and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny))

    res = 0
    for row in visited:
        res += row.count(0)
    answer += res 

print(answer)
