import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().strip().split())
pan = [list(map(int, input().strip().split())) for _ in range(N)]
where_mane = deque([])
where_chair = set()
where_wall = set()
for n in range(N):
    for m in range(M):
        if pan[n][m] == 4:
            start = (n, m)
        elif pan[n][m] == 3:
            where_mane.append((n, m))
        elif pan[n][m] == 2:
            where_chair.add((n, m))
        elif pan[n][m] == 1:
            where_wall.add((n, m))

if not where_chair:
    print(-1)
    quit()

visited_mane = [[0 for _ in range(M)] for _ in range(N)]
for x, y in where_mane:
    visited_mane[x][y] = 1
    pan[x][y] = 0

while where_mane:
    x, y = where_mane.popleft()
    for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
        nx, ny = x + dx, y + dy
        if N > nx >= 0 and M > ny >= 0 and visited_mane[nx][ny] == 0 and visited_mane[x][y] <= K:
            visited_mane[nx][ny] = visited_mane[x][y] + 1
            where_mane.append((nx, ny))
            

q = deque([(start[0], start[1], 0)])
visited = [[0 for _ in range(M)] for _ in range(N)]
visited[start[0]][start[1]] = 1
while q:
    x, y, c = q.popleft()
    if (x, y) in where_chair:
        print(c)
        quit()

    for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
        nx, ny = x + dx, y + dy
        if N > nx >= 0 and M > ny >= 0 and (nx, ny) not in where_wall and not visited_mane[nx][ny] and not visited[nx][ny]:
            q.append((nx, ny, c+1))
            visited[nx][ny] = 1
            
print(-1)
