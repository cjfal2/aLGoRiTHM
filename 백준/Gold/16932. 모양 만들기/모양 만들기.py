from collections import deque
import sys
input = sys.stdin.readline


dix = ((1, 0), (-1, 0), (0, 1), (0, -1))


def bfs_one(i, j, k):
    kan = 1
    q = deque([(i, j)])
    visited[i][j] = k
    while q:
        x, y = q.popleft()
        for dx, dy in dix:
            nx, ny = x + dx, y + dy
            if N > nx >= 0 and M > ny >= 0 and pan[nx][ny] and not visited[nx][ny]:
                q.append((nx, ny))
                kan += 1
                visited[nx][ny] = k
    zeros[k] = kan


def caz(i, j):
    kan = 1
    memo = set()
    for dx, dy in dix:
        nx, ny = i + dx, j + dy
        if N > nx >= 0 and M > ny >= 0 and pan[nx][ny] == 1 and visited[nx][ny] not in memo:
            a = visited[nx][ny]
            kan += zeros.get(a)
            memo.add(a)
    return kan


N, M = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
zeros = dict()

k = 1
for n in range(N):
    for m in range(M):
        if pan[n][m] and not visited[n][m]:
            k += 1
            bfs_one(n, m, k)

max_kan = 0
for n in range(N):
    for m in range(M):
        if not pan[n][m]:
            max_kan = max(max_kan, caz(n, m))

print(max_kan)