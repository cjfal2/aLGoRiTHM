import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().strip().split())
pan = [list(map(int, input().strip().split())) for _ in range(N)]

total = 0
for n in range(N):
    for m in range(M):
        if pan[n][m]:
            total += 1
            q = deque()
            q.append((n, m))
            pan[n][m] = 0
            while q:
                x, y = q.popleft()
                for dx, dy in [[1, 0],[-1, 0],[0, 1],[0, -1],[1, 1],[-1, -1],[-1, 1],[1, -1]]:
                    nx, ny = x + dx, y + dy
                    if N > nx >= 0 and M > ny >= 0 and pan[nx][ny]:
                        q.append((nx, ny))
                        pan[nx][ny] = 0
print(total)