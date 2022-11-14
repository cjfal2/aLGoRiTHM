import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().strip().split())
maze = []
hole = []
for idx_N in range(N):
    jool = list(input().strip().replace(".", "@"))
    maze.append(jool)
    for idx_M in range(M):
        if idx_N == 0 or idx_N == N-1:
            if jool[idx_M] == "@":
                hole.append((idx_N, idx_M))
        else:
            if idx_M == 0 or idx_M == M-1:
                if jool[idx_M] == "@":
                    hole.append((idx_N, idx_M))
                    
hole_s, hole_e = hole

visited = [[0 for _ in range(M)] for _ in range(N)]
visited[hole_s[0]][hole_s[1]] = 1

q = [(hole_s[0], hole_s[1])]
while q:
    x, y = q.pop(0)
    for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        nx, ny = x + dx, y + dy
        if N > nx >= 0 and M > ny >= 0 and not visited[nx][ny] and maze[nx][ny] == "@":
            q.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1

q = [(hole_e[0], hole_e[1])]
maze[hole_e[0]][hole_e[1]] = "."
while q:
    x, y = q.pop(0)
    for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        nx, ny = x + dx, y + dy
        if N > nx >= 0 and M > ny >= 0 and visited[nx][ny] == visited[x][y] - 1 and maze[nx][ny] == "@":
            q.append((nx, ny))
            maze[nx][ny] = '.'

for v in maze:
    print(*v, sep="")