from collections import deque
from sys import stdin
input = stdin.readline

N, M, K = map(int, input().strip().split())
pan = [list(map(int, input().strip())) for _ in range(N)]
dix = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs():
    visited = [[[0 for _ in range(K + 1)] for _ in range(M)] for _ in range(N)]
    visited[0][0][K] = 1

    q = deque([(0, 0, K)])

    while q:
        x, y, w = q.popleft()

        # 도착
        if x == N - 1 and y == M - 1:
            return visited[x][y][w]

        for dx, dy in dix:
            nx, ny = x + dx, y + dy

            if N > nx >= 0 and M > ny >= 0:
                # 현재 위치가 벽이고, 벽을 아직 부수지 않았으며 K개를 초과하지 않는 경우
                if pan[nx][ny] == 1 and w > 0 and visited[nx][ny][w - 1] == 0:
                    visited[nx][ny][w - 1] = visited[x][y][w] + 1
                    q.append((nx, ny, w - 1))

                # 현재 위치가 길이고, 아직 방문하지 않았다면
                elif pan[nx][ny] == 0 and visited[nx][ny][w] == 0:
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    q.append((nx, ny, w))

    return -1


print(bfs())
