import sys
input = sys.stdin.readline
from collections import deque

dix = {
    '-': [(0, 1), (0, -1)],
    '|': [(-1, 0), (1, 0)],
    '+': [(0, 1), (0, -1), (1, 0), (-1, 0)]
}


def bfs():
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[0][0] = 1
    q = deque()
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        for dx, dy in dix.get(pan[x][y]):
            nx, ny = x + dx, y + dy
            if N > nx >= 0 and M > ny >= 0 and not visited[nx][ny] and pan[nx][ny] != '*':
                if nx == N-1 and ny == M-1:
                    return visited[x][y]+1
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
    return -1

for _ in range(int(input().strip())):
    N = int(input().strip())
    M = int(input().strip())
    pan = [list(input().strip()) for _ in range(N)]
    if N == M == 1:
        print(1)
        continue
    print(bfs())
