N, M = map(int, input().split())
pan = []
starts = []
dots = 0
for n in range(N):
    temp = input()
    pan.append(temp)
    for m in range(M):
        if temp[m] == "X" or temp[m] == " ":
            continue
        elif temp[m] == ".":
            dots += 1
        else:
            starts.append((n, m))

visited = [[0 for _ in range(M)] for _ in range(N)]
answer = 0
for n, m in starts:
    q = [(n, m)]
    visited[n][m] = 1
    flag = False
    while q:
        x, y = q.pop(0)
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nx, ny = x + dx, y + dy
            if N > nx >= 0 and M > ny >= 0 and not visited[nx][ny] and pan[nx][ny] in (".", " "):
                visited[nx][ny] = 1
                q.append((nx, ny))
                if pan[nx][ny] == ".":
                    dots -= 1
                    flag = True
    if flag:
        answer += 1
print(answer, dots)