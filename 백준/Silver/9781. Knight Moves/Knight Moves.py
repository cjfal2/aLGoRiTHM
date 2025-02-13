import sys
from collections import deque

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

input = sys.stdin.readline

def bfs(n, m, grid, start, end):
    visited = [[False] * m for _ in range(n)]
    queue = deque()
    queue.append((start[0], start[1], 0))
    visited[start[0]][start[1]] = True

    while queue:
        x, y, dist = queue.popleft()
        if (x, y) == end:
            return dist

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] != '#':
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))
    return -1

n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

start, end = None, None
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'K':
            start = (i, j)
        elif grid[i][j] == 'X':
            end = (i, j)

print(bfs(n, m, grid, start, end))
