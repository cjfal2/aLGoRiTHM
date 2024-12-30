N, M = map(int, input().split())
pan = [list(input()) for _ in range(N)]
q = [(0, 0, [(1, 1)])]
visited = [[0 for _ in range(M)] for _ in range(N)]
while q:
    x, y, route = q.pop(0)
    if (x, y) == (N-1, M-1):
        for r in route:
            print(*r)
        break

    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nx = x + dx
        ny = y + dy
        if N > nx >= 0 and 0 <= ny < M and not visited[nx][ny] and pan[nx][ny] == ".":
            visited[nx][ny] = True
            q.append((nx, ny, route + [(nx+1, ny+1)]))
