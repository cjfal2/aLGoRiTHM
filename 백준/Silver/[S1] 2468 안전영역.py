N = int(input())
pan = []
for _ in range(N):
    L = list(map(int, input().split()))
    pan.append(L)
co = []
for A in range(101):
    visited = [[False for _ in range(N)] for _ in range(N)]
    su = 0
    for i in range(N):
        for j in range(N):
            if pan[i][j] > A and not visited[i][j]:
                visited[i][j] = True
                q = [(i, j)]
                while q:
                    x, y = q.pop(0)
                    for dx, dy in [[1, 0],[-1, 0], [0, 1], [0, -1]]:
                        nx, ny = x+dx, y+dy
                        if N > nx >= 0 and N > ny >= 0 and not visited[nx][ny] and pan[nx][ny] > A:
                            visited[nx][ny] = True
                            q.append((nx, ny))
                su += 1
    co.append(su)
print(max(co))
