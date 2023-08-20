import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().strip().split())
pan = []
q = deque([])
visited = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    temp = list(map(int, input().strip().split()))
    for j in range(M):
        if temp[j] in [1, 2]:
            q.append((i, j, temp[j], 1))
            visited[i][j] = 1
    pan.append(temp)

while q:
    x, y, w, v = q.popleft()
    if pan[x][y] != 3:
        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            nx, ny = x + dx, y + dy
            if N > nx >= 0 and M > ny >= 0 and pan[nx][ny] != -1:
                if pan[nx][ny] == 0:
                    pan[nx][ny] = w
                    visited[nx][ny] = v + 1
                    q.append((nx, ny, w, v + 1))
                elif pan[nx][ny] != w and visited[nx][ny] == v + 1:
                    pan[nx][ny] = 3

one, two, three = 0, 0, 0

for v in pan:
    for m in v:
        if m == 1:
            one += 1
        elif m == 2:
            two += 1
        elif m == 3:
            three += 1

print(one, two, three)
