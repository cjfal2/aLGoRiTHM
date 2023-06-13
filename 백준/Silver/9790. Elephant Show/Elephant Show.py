while 1:
    M, N = map(int, input().split())
    if M==N==0:
        break
    sx, sy = -1, -1
    pan = []
    for i in range(N):
        p = list(input())
        if sx == sy == -1:
            for j in range(M):
                if p[j] == "A":
                    sx, sy = i, j
                    p[j] = "."
        pan.append(p)
    cnt = 0
    q = [(sx, sy)]
    while q:
        x, y = q.pop(0)
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nx, ny = x + dx, y + dy
            if N > nx >= 0 and M > ny >= 0 and pan[nx][ny] == ".":
                pan[nx][ny] = "#"
                q.append((nx, ny))
                cnt += 1
    print(cnt)