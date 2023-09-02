from collections import deque
import sys
input = sys.stdin.readline

dix = [(1, 0), (-1, 0), (0, 1), (0, -1)]

N, M, K = map(int, input().split())
pan = [list(map(int, input().strip())) for _ in range(N)]

visited = [[[sys.maxsize for _ in range(K + 1)] for _ in range(M)] for _ in range(N)]
visited[0][0][K] = 0

q = deque([(0, 0, 1, K)])

answer = sys.maxsize

while q:
    x, y, time, w = q.popleft()
    if x == N - 1 and y == M - 1:
        answer = min(answer, time)
        continue

    morning = time % 2
    for dx, dy in dix:
        nx, ny = x + dx, y + dy
        if N > nx >= 0 and M > ny >= 0:
            if pan[nx][ny] == 1 and w > 0 and visited[nx][ny][w-1] > time:
                if morning:
                    visited[nx][ny][w-1] = time
                    q.append((nx, ny, time + 1, w - 1))
                else:
                    q.append((x, y, time + 1, w))

            if pan[nx][ny] == 0 and visited[nx][ny][w] > time:
                visited[nx][ny][w] = time
                q.append((nx, ny, time + 1, w))


print(answer if answer < sys.maxsize else -1)
