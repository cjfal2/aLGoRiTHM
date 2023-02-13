import sys
input = sys.stdin.readline
from collections import deque

for _ in range(int(input().strip())):
    N = int(input())
    pan = [list(input().strip()) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    white = []
    for n in range(N):
        for m in range(N):
            if pan[n][m] == "w" and not visited[n][m]:
                num = 0
                visited[n][m] = 1
                q = deque([(n, m)])
                while q:
                    x, y = q.popleft()
                    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1):
                        nx, ny = x + dx, y + dy
                        if N > nx >= 0 and N > ny >= 0 and not visited[nx][ny] and pan[nx][ny] != 'b':
                            if pan[nx][ny] == "-":
                                num += 1
                            visited[nx][ny] = 1
                            q.append((nx, ny))
                white.append(num)
    print(max(white))