import sys
input = sys.stdin.readline
from collections import deque

pan = []
start, end = 0, 0
for i in range(10):
    a = input().strip()
    for j in range(10):
        if a[j] == "B":
            start = (i, j)
        elif a[j] == "L":
            end = (i, j)
    pan.append(a)

visited = [[0 for _ in range(10)] for _ in range(10)]
visited[start[0]][start[1]] = 1
q = [start]
while q:
    x, y = q.pop(0)
    if x == end[0] and y == end[1]:
        print(visited[x][y]-2)
        quit()
    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
        nx, ny = x + dx, y + dy
        if 10 > nx >= 0 and 10 > ny >= 0 and not visited[nx][ny] and pan[nx][ny] != "R":
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))
                        
