from collections import deque
import sys
input = sys.stdin.readline


N, M = map(int, input().strip().split())

pan = []
flag = True

for i in range(N):
    pp = input().strip()
    if flag:
        for j in range(M):
            if pp[j] == 'z':
                sx, sy = i, j
                flag = False
                q = deque()
                q.append((i, j))
                visited = [[0 for _ in range(M)] for _ in range(N)]
                visited[i][j] = 1
                break
    pan.append(pp)

while q:
    x, y = q.popleft()
    for dx, dy in (1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1):
        nx, ny = x + dx, y + dy
        if N > nx >= 0 and M > ny >= 0 and not visited[nx][ny] and pan[nx][ny] != 'x':
            if pan[nx][ny] == 'n':
                print(visited[x][y])
                quit()
            q.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1

print("NIE")
