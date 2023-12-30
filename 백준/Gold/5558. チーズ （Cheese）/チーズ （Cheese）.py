N, M, K = map(int, input().split())
pan = []
sx, sy = 0, 0
for n in range(N):
    temp = input()
    if not sx and not sy:
        for m in range(M):
            if temp[m] == "S":
                sx, sy = n, m
    pan.append(temp)

visited = [[-1 for _ in range(M)] for _ in range(N)]
visited[sx][sy] = 0
q = [(sx, sy)]
answer = 0
target = 1
while q:
    if target > K:
        break

    x, y = q.pop(0)
    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
        nx, ny = x + dx, y + dy
        if N > nx >= 0 and M > ny >= 0 and visited[nx][ny] == -1 and pan[nx][ny] != "X":
            if pan[nx][ny] == str(target):
                answer += (visited[x][y] + 1)
                visited = [[-1 for _ in range(M)] for _ in range(N)]
                visited[nx][ny] = 0
                q = [(nx, ny)]
                target += 1
                # print(answer)
                break
            else:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
print(answer)