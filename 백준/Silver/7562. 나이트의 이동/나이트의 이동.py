import sys
input = sys.stdin.readline
from collections import deque


for tc in range(int(input().strip())):
    N = int(input().strip())
    pan = [[0 for _ in range(N)] for _ in range(N)]
    sx, sy = map(int, input().strip().split())
    ex, ey = map(int, input().strip().split())

    q = deque([(sx, sy)])
    pan[sx][sy] = 1
    while q:
        x, y = q.popleft()
        if x == ex and y == ey:
            print(pan[x][y]-1)
            break

        for dx, dy in (-2,-1), (-2,1), (-1,-2), (-1,2), (1,-2), (1,2), (2,-1), (2,1):
            nx, ny = x + dx, y + dy
            if N > nx >= 0 and N > ny >= 0 and not pan[nx][ny]:
                pan[nx][ny] = pan[x][y] + 1
                q.append((nx, ny))
