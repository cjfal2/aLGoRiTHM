import sys
input = sys.stdin.readline


N, M = map(int, input().strip().split())

pan = []
flag = True

for i in range(N):
    pp = list(input().strip())
    if flag:
        for j in range(M):
            if pp[j] == 'z':
                sx, sy = i, j
                flag = False
                q = [(i, j)]
                visited = [[0 for _ in range(M)] for _ in range(N)]
                visited[i][j] = 1
                break
    pan.append(pp)

while q:
    x, y = q.pop(0)
    if pan[x][y] == 'n':
        print(visited[x][y]-1)
        quit()
    for dx, dy in (1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1):
        nx, ny = x + dx, y + dy
        if N > nx >= 0 and M > ny >= 0 and not visited[nx][ny] and pan[nx][ny] != 'x':
            q.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1

print("NIE")
