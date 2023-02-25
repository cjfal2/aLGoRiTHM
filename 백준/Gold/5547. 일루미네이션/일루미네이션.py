oddeven = {
    0: [(-1, -1), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 0)], # 짝
    1: [(-1, 1), (-1, 0), (0, 1), (0, -1), (1, 1), (1, 0)], # 홀
}


def check_around(p, q):
    global ans
    for dp, dq in oddeven.get(p%2):
        np, nq = p + dp, q + dq
        if pan[np][nq] == 1:
            ans += 1


def bfs_zero(i, j):
    q = [(i, j)]
    visited[i][j] = 1
    check_around(i, j)
    while q:
        x, y = q.pop(0)
        for dx, dy in oddeven.get(x%2):
            nx, ny = x + dx, y + dy
            if not visited[nx][ny] and pan[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = 1
                check_around(nx, ny)


def bfs_one(i, j):
    global ans
    q = [(i, j)]
    visited[i][j] = 1
    while q:
        x, y = q.pop(0)
        for dx, dy in oddeven.get(x%2):
            nx, ny = x + dx, y + dy
            if not visited[nx][ny]:
                if pan[nx][ny] == 1:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                elif pan[nx][ny] == 2:
                    ans += 1


M, N = map(int, input().split())
pan = [[2 for _ in range(M+2)]] +  [[2] + list(map(int, input().split())) + [2] for _ in range(N)] + [[2 for _ in range(M+2)]]
visited = [[0 for _ in range(M+2)] for _ in range(N+2)]

ans = 0

for n in (1, N):
    for m in range(1, M+1):
        if not visited[n][m]:
            bfs_one(n, m) if pan[n][m] else bfs_zero(n, m)

for m in (1, M):
    for n in range(2, N):
        if not visited[n][m]:
            bfs_one(n, m) if pan[n][m] else bfs_zero(n, m)

print(ans)