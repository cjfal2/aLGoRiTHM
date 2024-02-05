# 얼음 미로
import sys
import heapq
input = sys.stdin.readline

dix = ((1, 0), (-1, 0), (0, 1), (0, -1))
M, N = map(int, input().strip().split())
holes = [["H" for _ in range(M+2)]]
pan = []
for n in range(1, N+1):
    arr = ["H"] + list(input().strip()) + ["H"]
    pan.append(arr)
    for m in range(1, M+1):
        if arr[m] == "T":
            sx, sy = n, m
        elif arr[m] == "E":
            ex, ey = n, m

pan = holes + pan + holes
pan[sx][sy] = "H"

visited = [[99999999 for _ in range(M+2)] for _ in range(N+2)]
visited[sx][sy] = 0

q = []
heapq.heappush(q, (0, sx, sy))

answer = 99999999
while q:
    cnt, x, y = heapq.heappop(q)
    if visited[x][y] < cnt:
        continue

    for dx, dy in dix:
        now_cnt = cnt
        nx, ny = x, y
        while 1:
            nx += dx
            ny += dy
            if N >= nx > 0 and M >= ny > 0:
                temp = pan[nx][ny]
                if temp == "H":
                    break

                if temp in "RE":
                    if temp == "R":
                        nx -= dx
                        ny -= dy
                    if visited[nx][ny] > now_cnt:
                        visited[nx][ny] = now_cnt
                        heapq.heappush(q, (now_cnt, nx, ny))
                    break

                now_cnt += int(temp)
            else:
                break

answer = visited[ex][ey]
print(answer if answer != 99999999 else -1)
