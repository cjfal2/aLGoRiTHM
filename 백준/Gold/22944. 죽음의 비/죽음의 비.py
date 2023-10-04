import sys
from collections import deque

input = sys.stdin.readline

N, H, D = map(int, input().strip().split())
pan = []
flag = True
for i in range(N):
    temp = list(input().strip())
    if flag:
        for j in range(N):
            if temp[j] == 'S':
                sx, sy, flag = i, j, False
    pan.append(temp)


visited = [[0 for _ in range(N)] for _ in range(N)]
q = deque([(sx, sy, H, 0, 0)]) # x좌표, y좌표, 피, 우산 피, 거리
visited[sx][sy] = H

while q:
    x, y, h, d, cnt = q.popleft()

    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
        nx, ny = x + dx, y + dy

        if N > nx >= 0 and N > ny >= 0:
            if pan[nx][ny] == 'E': # 안전지대
                print(cnt+1)
                quit()

            nh, nd = h, d

            if pan[nx][ny] == 'U':
                nd = D

            if nd == 0:
                nh -= 1
            else:
                nd -= 1

            if nh == 0:
                continue

            if visited[nx][ny] < nh:
                visited[nx][ny] = nh
                q.append((nx, ny, nh, nd, cnt+1))

print(-1)
