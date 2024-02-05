import sys
import heapq
input = sys.stdin.readline


M, N = map(int, input().split())
pan = []
where_c = []
for n in range(N):
    arr = list(input().strip())
    pan.append(arr)
    for m in range(M):
        if arr[m] == "C":
            where_c.append((n, m))

sx, sy = where_c[0]
ex, ey = where_c[1]
mirrors = [[sys.maxsize] * M for _ in range(N)]
visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(2)]
q = []
dix = ((1, 0), (0, 1), (-1, 0), (0, -1))


heapq.heappush(q, (-1, sx, sy))
pan[sx][sy] = '*'

while q:
    cnt, x, y = heapq.heappop(q)
    cnt += 1
    for d in range(4):
        dx, dy = dix[d]
        nx, ny = x, y
        while 1:
            nx += dx
            ny += dy
            if N > nx >= 0 and M > ny >= 0:
                if pan[nx][ny] == '.':
                    if mirrors[nx][ny] > cnt:
                        mirrors[nx][ny] = cnt
                        visited[d % 2][nx][ny] = 1
                        heapq.heappush(q, (cnt, nx, ny))

                    elif mirrors[nx][ny] == cnt and visited[d % 2][nx][ny] == False:
                        mirrors[nx][ny] = cnt
                        visited[d % 2][nx][ny] = 1
                        heapq.heappush(q, (cnt, nx, ny))

                    else:
                        break

                elif pan[nx][ny] == '*':
                    break

                elif pan[nx][ny] == 'C':
                    print(cnt)
                    quit()
            else:
                break
