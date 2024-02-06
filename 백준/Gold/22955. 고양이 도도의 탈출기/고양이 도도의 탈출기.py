# 백준 22955번 고양이 도도
import heapq
import sys
input = sys.stdin.readline


dx = [0, 0]
dy = [1, -1]
N, M = map(int, input().strip().split())
pan, where_X = [], []
for x in range(N):
    arr = list(input().strip())
    for y in range(M):
        if arr[y] == 'C':
            arr[y] = 'F'
            sx, sy = x, y
        elif arr[y] == 'X':
            where_X.append((x, y))
    pan.append(arr)

# 떨어질 지점 전처리
for fx, fy in where_X:
    if pan[fx][fy] == 'X':
        temp = []
        temp.append([fx, fy])
        nx = fx
        while 1:
            nx += 1
            if pan[nx][fy] != 'X':
                break
            temp.append([nx, fy])

        # 개다 => 다 바꿈
        if pan[nx][fy] == 'D':
            for px, py in temp:
                pan[px][py] = 'D'

        # 바닥 => 좌표를 바닥 좌표로 변경
        else:
            for px, py in temp:
                pan[px][py] = [nx, fy]

big = sys.maxsize
visited = [[big for _ in range(M)] for _ in range(N)]
visited[sx][sy] = 0
q = []
heapq.heappush(q, [0, sx, sy])
answer = big
while q:
    cnt, x, y = heapq.heappop(q)
    if cnt > visited[x][y]:  # 다익스트라
        continue
    
    where = pan[x][y]
    if where == 'E':  # 도착했다면
        answer = cnt
        break

    # 지금 평지에 있다면
    if where == 'F' or where == "L":
        for dx, dy in (0, 1), (0, -1):
            nx, ny = x + dx, y + dy
            if N > nx >= 0 and M > ny >= 0 and pan[nx][ny] != 'D' and visited[nx][ny] > cnt+1:
                visited[nx][ny] = cnt+1
                heapq.heappush(q, (cnt+1, nx, ny))

        if x+1 < N and pan[x+1][y] == 'L' and visited[x+1][y] > cnt+5:
            visited[x+1][y] = cnt+5
            heapq.heappush(q, (cnt+5, x+1, y))

        # 평지인데 사다리라면
        if where == 'L' and x-1 >= 0 and not pan[x-1][y] == 'D' and visited[x-1][y] > cnt+5:
            visited[x-1][y] = cnt+5
            heapq.heappush(q, (cnt+5, x-1, y))

    # 지금 구역이 X --> 전처리한 끝좌표로 내려감.
    else:
        nx = pan[x][y][0]
        ny = pan[x][y][1]

        if visited[nx][ny] > cnt+10:
            visited[nx][ny] = cnt+10
            heapq.heappush(q, (cnt+10, nx, ny))

print(answer if answer != big else 'dodo sad')
