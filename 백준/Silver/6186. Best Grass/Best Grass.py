N, M = map(int, input().split())

pan = [list(input()) for _ in range(N)]
num = 0
for n in range(N):
    for m in range(M):
        if pan[n][m] == "#":
            num += 1
            pan[n][m] = "."
            q = [(n, m)]
            while q:
                x, y = q.pop(0)
                for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                    nx, ny = x + dx, y + dy
                    if N > nx >= 0 and M > ny >= 0 and pan[nx][ny] == "#":
                        pan[nx][ny] = "."
                        q.append((nx, ny))
print(num)