from collections import deque


N, M = map(int, input().split())
fx, fy, hx, hy = map(lambda x: int(x) - 1, input().split()
                     )  # (fx, fy): 개구리 위치, (hx, hy): 집 위치
if fx == hx and fy == hy:
    print(0)
    quit()

elif fx == hx or fy == hy:
    print(1)
    quit()

pan = [list(map(int, input().split())) for _ in range(N)]

visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
visited_n = [0 for _ in range(N)]
visited_m = [0 for _ in range(M)]
visited[0][0][0] = 1

q = deque([(fx, fy, 0, 0)])

answer = 0
flag = 0
while q:
    x, y, cnt, skill = q.popleft()
    jump = pan[x][y]
    if x == hx and y == hy:
        answer, flag = cnt, 1
        break

    if skill == 0:
        if not visited_n[x]:
            visited_n[x] = 1
            for m in range(M):
                if not visited[x][m][1]:
                    visited[x][m][1] = 1
                    q.append((x, m, cnt+1, 1))

        if not visited_m[y]:
            visited_m[y] = 1
            for n in range(N):
                if not visited[n][y][1]:
                    visited[n][y][1] = 1
                    q.append((n, y, cnt+1, 1))

    for nx, ny in (x+jump, y), (x-jump, y), (x, y+jump), (x, y-jump):
        if N > nx >= 0 and M > ny >= 0 and not visited[nx][ny][skill]:
            visited[nx][ny][skill] = 1
            q.append((nx, ny, cnt + 1, skill))

if flag:
    print(answer)
else:
    print(-1)