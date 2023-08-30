from collections import deque
import sys
input = sys.stdin.readline


def bfs(v, q):
    while q:
        x, y = q.popleft()

        for dx, dy in direction:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M and not v[nx][ny] and pan[nx][ny]:
                if nx == N - 1:
                    print(v[x][y])
                    return

                v[nx][ny] = v[x][y] + 1
                q.append((nx, ny))
    print(-1)


N, M = map(int, input().strip().split())
pan = [list(map(int, input().strip().split())) for _ in range(N)]
direction = []

for _ in range(int(input().strip())):
    direction.append(tuple(map(int, input().strip().split())))

visited = [[0 for _ in range(M)] for _ in range(N)]
queue = deque([])

for m in range(M):
    if pan[0][m] == 1:
        queue.append((0, m))
        visited[0][m] = 1

bfs(visited, queue)
