import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().strip().split())
sx, sy, ex, ey = map(lambda x: int(x) - 1, input().strip().split())
pan = []
for i in range(N):
    pan.append(input().strip())

visited = [[0 for _ in range(M)] for _ in range(N)]
visited[sx][sy] = 1

q = []
heapq.heappush(q, (0, sx, sy))

answer = 0
while q:
    cnt, x, y = heapq.heappop(q)
    if x == ex and y == ey:
        answer = cnt + 1
        break

    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
        nx, ny = x + dx, y + dy
        if N > nx >= 0 and M > ny >= 0 and not visited[nx][ny]:
            visited[nx][ny] = 1
            heapq.heappush(q, (cnt+1, nx, ny)) if pan[nx][ny] == "1" else heapq.heappush(q, (cnt, nx, ny))
print(answer)
