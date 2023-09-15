from collections import deque


def bfs():
    q = deque([(0, 0, 0, K)])

    visited = [[[0 for _ in range(K+1)] for _ in range(M)] for _ in range(N)]
    visited[0][0][K] = 1

    while q:
        x, y, cnt, k = q.popleft()

        if x == N - 1 and y == M - 1:
            print(cnt)
            return

        if k > 0:
            for dx, dy in (-1, -2), (-1, 2), (1, -2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1):
                nx, ny = x + dx, y + dy
                if N > nx >= 0 and M > ny >= 0 and pan[nx][ny] == 0 and not visited[nx][ny][k - 1]:
                    q.append((nx, ny, cnt + 1, k - 1))
                    visited[nx][ny][k - 1] = 1

        for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and pan[nx][ny] == 0 and not visited[nx][ny][k]:
                q.append((nx, ny, cnt + 1, k))
                visited[nx][ny][k] = 1

    print(-1)


K = int(input())
M, N = map(int, input().split())  # 가로길이, 세로길이
pan = [list(map(int, input().split())) for _ in range(N)]
bfs()
