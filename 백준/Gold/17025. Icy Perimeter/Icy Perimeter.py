N = int(input())
M = N+2
z = "." * (M)
pan = [z]
for _ in range(N):
    t = "." + input() + "."
    pan.append(t)
pan.append(z)

visited = [[0 for _ in range(M)] for _ in range(M)]

answer = []
for i in range(1, M):
    for j in range(1, M):
        if not visited[i][j] and pan[i][j] == "#":
            visited[i][j] = 1
            q = [(i, j)]
            total = 1
            side = 0
            while q:
                x, y = q.pop(0)
                for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                    nx, ny = x + dx, y + dy
                    if M > nx >= 0 and M > ny >= 0 and not visited[nx][ny]:
                        if pan[nx][ny] == ".":
                            side += 1
                        else:
                            visited[nx][ny] = 1
                            q.append((nx, ny))
                            total += 1
            answer.append((total, side))
answer.sort(key=lambda x: (x[0] * -1, x[1]))
print(*answer[0])