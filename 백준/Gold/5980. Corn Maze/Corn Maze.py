N, M = map(int, input().split())
pan = []
w = dict()
for i in range(N):
    ip = input()
    for j in range(M):
        if ip[j] == "@":
            sx, sy = i, j
        elif ip[j] != '.' and ip[j] != '=' and ip[j] != '#':
            if not w.get(ip[j]):
                w[ip[j]] = [(i, j)]
            else:
                w[ip[j]].append((i, j))
    pan.append(ip)

visited = [[0 for _ in range(M)] for _ in range(N)]
visited[sx][sy] = 1
q = [(sx, sy, 0)]
while q:
    x, y, d = q.pop(0)
    if pan[x][y] == '=':
        print(d)
        quit()
    for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        nx, ny = x + dx, y + dy
        if N > nx >= 0 and M > ny >= 0 and not visited[nx][ny] and pan[nx][ny] != '#':
            if pan[nx][ny] != '.' and pan[nx][ny] != '=' and pan[nx][ny] != '#':
                for i, j in w.get(pan[nx][ny]):
                    if (nx, ny) != (i, j):
                        nx, ny = i, j
                        break
            else:
                visited[nx][ny] = 1
            q.append((nx, ny, d+1))
