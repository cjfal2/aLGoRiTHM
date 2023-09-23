pan = [list(map(int, input().split())) for _ in range(5)]
s = tuple(map(int, input().split()))
visited = [[0 for _ in range(5)] for _ in range(5)]

a = []
def dfs(x, y, depth, apple):
    visited[x][y] = 1
    
    for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
        nx, ny = x + dx, y + dy
        if 5 > nx >= 0 and 5 > ny >= 0 and pan[nx][ny] != -1 and not visited[nx][ny]:
            if pan[nx][ny] == 1:
                if apple >= 2:
                    a.append(depth+1)
                    return
                
                pan[nx][ny] = -1
                dfs(nx, ny, depth+1, apple+1)
                pan[nx][ny] = 1
                visited[nx][ny] = 0
            else:
                pan[nx][ny] = -1
                dfs(nx, ny, depth+1, apple)
                pan[nx][ny] = 0
                visited[nx][ny] = 0

dfs(*s, 0, 0)
print(min(a)) if a else print(-1)
