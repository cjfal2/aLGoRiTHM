from collections import deque
from itertools import combinations

def bfs():
    visited = [[0 for _ in range(M)] for _ in range(N)]
    kill = 0

    for n in range(N):
        for m in range(M):
            if pan[n][m] == 2 and not visited[n][m]:
                flag = True
                q = deque([(n, m)])
                visited[n][m] = 1
                num = 0

                while q:
                    num += 1
                    x, y = q.popleft()

                    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                        nx = x + dx
                        ny = y + dy

                        if N > nx >= 0 and M > ny >= 0:
                            if pan[nx][ny] == 0:
                                flag = False
                            elif pan[nx][ny] == 2 and visited[nx][ny] == 0:
                                visited[nx][ny] = 1
                                q.append((nx, ny))

                if flag:
                    kill += num

    return kill


N, M = map(int, input().split())
pan = []
deca = []

for i in range(N):
    R = list(map(int, input().split()))
    pan.append(R)

    for j in range(M):
        if not R[j]:
            deca.append((i, j))

ans = 0

for i, j in combinations(list(range(len(deca))), 2):
    dx1, dy1 = deca[i]
    dx2, dy2 = deca[j]

    pan[dx1][dy1] = 1
    pan[dx2][dy2] = 1

    ans = max(bfs(), ans)

    pan[dx1][dy1] = 0
    pan[dx2][dy2] = 0

print(ans)
