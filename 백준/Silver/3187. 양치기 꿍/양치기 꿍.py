N, M = map(int, input().split())
pan = [list(input()) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

sheep_t = 0
wolf_t = 0
for i in range(N):
    for j in range(M):
        if pan[i][j] != '#' and not visited[i][j]:
            visited[i][j] = 1
            q = [(i, j)]
            if pan[i][j] == 'k':
                sheep = 1
                wolf = 0
            elif pan[i][j] == 'v':
                sheep = 0
                wolf = 1
            else:
                sheep = 0
                wolf = 0

            while q:
                x, y = q.pop(0)
                for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    nx, ny = x + dx, y + dy
                    if N > nx >= 0 and M > ny >= 0 and not visited[nx][ny] and pan[nx][ny] != '#':
                        if pan[nx][ny] == 'k':
                            sheep += 1
                        elif pan[nx][ny] == 'v':
                            wolf += 1
                        q.append((nx, ny))
                        visited[nx][ny] = 1
            if sheep > wolf:
                sheep_t += sheep
            else:
                wolf_t += wolf
            

print(sheep_t, wolf_t)