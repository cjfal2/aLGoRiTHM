import heapq

N, M = map(int, input().split())
pan = []
sx, sy, ex, ey = -1, -1, -1, -1
for i in range(N):
    temp = list(input())
    for j in range(M):
        if temp[j] == "K":
            sx, sy = i, j
            
        if temp[j] == "*":
            ex, ey = i, j
            
    pan.append(temp)

if sx == sy == -1:
    print(-1)
    quit()

if ex == ey == -1:
    print(-1)
    quit()

visited = [[0 for _ in range(M)] for _ in range(N)]
visited[sx][sy] = 1

q = []
heapq.heappush(q, (0, sx, sy))

answer = 0
flag = False
while q:
    cnt, x, y = heapq.heappop(q)
    if x == ex and y == ey:
        answer = cnt
        flag = True
        break
    for dx, dy, fuel in [(1, 0, 1), (-1, 0, 1), (0, 1, 0), (0, -1, 1), (1, 1, 0), (-1, 1, 0), (1, -1, 1), (-1, -1, 1)]:
        nx, ny = x + dx, y + dy
        if N > nx >= 0 and M > ny >= 0 and not visited[nx][ny] and pan[nx][ny] != "#":
            visited[nx][ny] = 1
            heapq.heappush(q, (cnt+fuel, nx, ny))

print(answer if flag else -1)
