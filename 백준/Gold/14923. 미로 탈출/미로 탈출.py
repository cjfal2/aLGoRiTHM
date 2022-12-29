import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
Hx, Hy = map(int, input().split())
Ex, Ey = map(int, input().split())

pan = [list(map(int, input().split())) for _ in range(N)]

def bfs():
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    visited[Hx-1][Hy-1][0] = 1

    q = deque()
    q.append([Hx-1, Hy-1, 0])

    while q:
        x, y, w = q.popleft()

        # 도착
        if x == Ex-1 and y == Ey-1:
            return visited[x][y][w]-1

        for dx, dy in [[1, 0],[-1, 0],[0, 1],[0, -1]]:
            nx, ny = x + dx, y + dy

            if N > nx >= 0 and M > ny >= 0:
                # 현재 위치가 길이고, 아직 방문하지 않았다면
                if pan[nx][ny] == 0 and visited[nx][ny][w] == 0:
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    q.append([nx, ny, w])

                # 현재 위치가 벽이고, 벽을 아직 부수지 않았다면
                elif pan[nx][ny] == 1 and w == 0:
                    visited[nx][ny][w + 1] = visited[x][y][w] + 1
                    q.append([nx, ny, w + 1])
    return -1

print(bfs())
