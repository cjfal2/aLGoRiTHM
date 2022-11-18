M, N, K = map(int, input().split())
pan = [[0 for _ in range(N)] for _ in range(M)]
visited = [[0 for _ in range(N)] for _ in range(M)]
for _ in range(K):
    ws, hs, we, he = map(int, input().split())
    for h in range(hs, he):
        for w in range(ws, we):
            pan[h][w] = 1
total = 0
amount = []
for m in range(M):
    for n in range(N):
        if not visited[m][n] and not pan[m][n]:
            co = 1
            q = [(m, n)]
            visited[m][n] = 1
            while q:
                x, y = q.pop(0)
                for dx, dy in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
                    nx, ny = x + dx, y + dy
                    if M > nx >= 0 and N > ny >= 0 and not visited[nx][ny] and not pan[nx][ny]:
                        q.append((nx, ny))
                        visited[nx][ny] = 1
                        co += 1
            total += 1
            amount.append(co)
print(total)
amount.sort()
print(*amount)
