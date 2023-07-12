from collections import deque


N, M = map(int, input().split())
answer = [[0 for _ in range(M)] for _ in range(N)]

pan = []
flag = True
q = deque([])
sx, sy = 0, 0
for n in range(N):
    arr = list(map(int, input().split()))
    if flag:
        for m in range(M):
            if arr[m] == 2:
                flag = False
                answer[n][m] = 1
                sx, sy = n, m
                q.append((n, m, 0))
    pan.append(arr)


while q:
    x, y, distance = q.popleft()
    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
        nx, ny = x + dx, y + dy
        if N > nx >= 0 and M > ny >= 0 and answer[nx][ny] == 0 and pan[nx][ny] == 1:
            answer[nx][ny] = distance + 1
            q.append((nx, ny, distance + 1))

answer[sx][sy] = 0
for n in range(N):
    for m in range(M):
        if pan[n][m] == 1 and answer[n][m] == 0:
            print(-1, end=" ") if m < M - 1 else print(-1)
        else:
            print(answer[n][m], end=" ") if m < M - 1 else print(answer[n][m])