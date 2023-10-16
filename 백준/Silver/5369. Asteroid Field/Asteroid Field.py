def bfs():
    q = [(n, m)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[n][m] = 1
    while q:
        x, y = q.pop(0)
        for nx, ny in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
            if N > nx >= 0 and N > ny >= 0 and not visited[nx][ny] and pan[nx][ny] != "*":
                if pan[nx][ny] == "d":
                    return visited[x][y]
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
    return -1


for _ in range(int(input())):
    N = int(input())
    pan = [input() for _ in range(N)]
    for n in range(N):
        for m in range(N):
            if pan[n][m] == "s":
                print(bfs())