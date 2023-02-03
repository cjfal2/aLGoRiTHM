N, M = map(int, input().split())
donut = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for n in range(N):
    for m in range(M):
        if not donut[n][m]:
            ans += 1
            q = [(n, m)]
            donut[n][m] = 1
            while q:
                x, y = q.pop()
                for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                    nx, ny = x + dx, y + dy
                    if nx >= N:
                        nx = 0
                    elif 0 > nx:
                        nx = N-1
                    elif ny >= M:
                        ny = 0
                    elif 0 > ny:
                        ny = M-1
                    if not donut[nx][ny]:
                        donut[nx][ny] = 1
                        q.append((nx, ny))
print(ans)
