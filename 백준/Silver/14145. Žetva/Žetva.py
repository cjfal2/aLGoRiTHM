from collections import deque
import sys
input = sys.stdin.readline


def bfs(i, j):
    temp = set()
    temp.add((i, j))
    q = deque([(i, j)])
    while q:
        x, y = q.popleft()

        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and pan[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny))
                temp.add((nx, ny))

    return temp


N, M = map(int, input().strip().split())
pan = [list(map(int, input().strip())) for _ in range(N)]

info = []
visited = [[0 for _ in range(M)] for _ in range(N)]
for n in range(N):
    for m in range(M):
        if pan[n][m] and not visited[n][m]:
            visited[n][m] = 1
            info.append(bfs(n, m))

info.sort(key=lambda x: len(x))

for idx, arr in enumerate(info, 1):
    for x, y in arr:
        pan[x][y] = idx

for v in pan:
    print(*v, sep="")