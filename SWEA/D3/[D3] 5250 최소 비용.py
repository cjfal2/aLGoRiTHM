def bfs():
    visited = [[9999999] * N for _ in range(N)]
    visited[0][0] = 0
    q = [(0, 0)]
    while q:
        x, y = q.pop(0)
        for dx, dy in [[1,0],[-1,0],[0,1],[0,-1]]:
            nx = x + dx
            ny = y + dy
            if N > nx >= 0 and N > ny >= 0:
                high = 1
                if pan[nx][ny] > pan[x][y]:
                    high += (pan[nx][ny] - pan[x][y])

                if visited[nx][ny] > visited[x][y] + high:
                    visited[nx][ny] = visited[x][y] + high
                    q.append((nx,ny))

    return visited[N-1][N-1]

for tc in range(int(input())):
    N = int(input())
    pan = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc+1} {bfs()}')
