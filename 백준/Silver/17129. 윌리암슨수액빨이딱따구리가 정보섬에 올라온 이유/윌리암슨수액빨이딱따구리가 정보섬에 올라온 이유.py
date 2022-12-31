from collections import deque
import sys
input = sys.stdin.readline


N, M = map(int, input().strip().split())
jeongbo = []
flag = True
for i in range(N):
    a = input().strip()
    if flag:
        for j in range(M):
            if a[j] == '2':
                sn, sm = i, j
                flag = False
                break
    jeongbo.append(a)


visited = [[0 for _ in range(M)] for _ in range(N)]
visited[sn][sm] = 1
q = deque()
q.append((sn, sm))
while q:
    x, y = q.popleft()
    for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        nx, ny = x + dx, y + dy
        if N > nx >= 0 and M > ny >= 0 and not visited[nx][ny] and jeongbo[nx][ny] != '1':
            if jeongbo[nx][ny] != '0':
                print("TAK")
                print(visited[x][y])
                quit()
            q.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1
print("NIE")