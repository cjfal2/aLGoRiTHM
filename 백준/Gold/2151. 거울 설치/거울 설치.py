import sys
import heapq
input = sys.stdin.readline

N = int(input().strip())
pan = []
where_door = []
dix = ((0, 1), (1, 0), (0, -1), (-1, 0))  # 0우 1하 2좌 3상

for n in range(N):
    arr = list(input().strip())
    pan.append(arr)
    for m in range(N):
        if arr[m] == "#":
            where_door.append((n, m))

sx, sy = where_door[0]
ex, ey = where_door[1]
visited = [[[0 for _ in range(4)] for _ in range(N)] for _ in range(N)]

q = []
for k in range(4):
    heapq.heappush(q, (0, sx, sy, k))
    visited[sx][sy][k] = 1

answer = 99999
while q:
    cnt, x, y, d = heapq.heappop(q)
    dx, dy = dix[d]
    nx, ny = x + dx, y + dy
    if N > nx >= 0 and N > ny >= 0 and not visited[nx][ny][d] and pan[nx][ny] != "*":
        visited[nx][ny][d] = 1
        if pan[nx][ny] == "!":
            heapq.heappush(q, (cnt+1, nx, ny, (d+1) % 4))
            heapq.heappush(q, (cnt+1, nx, ny, (d-1) % 4))
            heapq.heappush(q, (cnt, nx, ny, d))
        elif pan[nx][ny] == ".":
            heapq.heappush(q, (cnt, nx, ny, d))
        elif pan[nx][ny] == "#":
            answer = min(cnt, answer)
print(answer)
