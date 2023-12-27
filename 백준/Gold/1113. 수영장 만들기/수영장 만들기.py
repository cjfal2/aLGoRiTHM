def bfs(i, j, h):
    visited[i][j] = 1
    low_land = [(i, j)]
    q = [(i, j)]
    flag = False
    while q:
        x, y = q.pop(0)
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nx, ny = x + dx, y + dy
            if N > nx >= 0 and M > ny >= 0:
                if not visited[nx][ny] and pan[nx][ny] < h:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    low_land.append((nx, ny))
            else:
                flag = True
    if flag:
        return 0

    for land in low_land:
        pan[land[0]][land[1]] += 1
    return len(low_land)


N, M = map(int, input().split())
pan = []
height = 0  # 벽 높이
for _ in range(N):
    temp = list(map(int, list(input())))
    height = max(height, max(temp))
    pan.append(temp)

answer = 0
for h in range(1, height+1):
    visited = [[0 for _ in range(M)] for _ in range(N)]
    for n in range(N):
        for m in range(M):
            if pan[n][m] < h and not visited[n][m]:
                answer += bfs(n, m, h)
print(answer)
