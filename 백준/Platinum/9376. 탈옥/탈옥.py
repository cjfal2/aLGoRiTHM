from collections import deque
import sys
input = sys.stdin.readline


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[x][y] = 1

    q = deque([(x, y)])

    while q:
        x, y = q.popleft()
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nx, ny = x + dx, y + dy
            if N > nx >= 0 and M > ny >= 0:
                if not visited[nx][ny]:
                    if pan[nx][ny] == '.':
                        visited[nx][ny] = visited[x][y]
                        q.appendleft((nx, ny))
                    elif pan[nx][ny] == '#':
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx, ny))

    return visited


for _ in range(int(input())):
    N, M = map(int, input().split())
    temp = []
    pan = [["." for _ in range(M+2)]]
    for i in range(N):
        w = list(input().strip())
        if len(temp) != 2:
            for j in range(M):
                if w[j] == "$":
                    temp.append((i+1, j+1))
                    w[j] = "."
        pan.append(["."] + w + ["."])
    pan.append(["." for _ in range(M+2)])

    N += 2
    M += 2

    sang = bfs(0, 0)
    prisoner_1 = bfs(*temp[0])
    prisoner_2 = bfs(*temp[1])

    answer = 99999999
    for i in range(N):
        for j in range(M):
            if sang[i][j] and prisoner_1[i][j] and prisoner_2[i][j]:
                cnt = sang[i][j] + prisoner_1[i][j] + prisoner_2[i][j] - 3
                if pan[i][j] == '#':
                    cnt -= 2
                answer = min(answer, cnt)
    print(answer)
