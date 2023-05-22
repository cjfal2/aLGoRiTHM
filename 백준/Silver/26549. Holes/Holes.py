def bfs(z, t):
    q = [(z, t)]
    pan[z][t] = "#"
    cnt = 1
    while q:
        x, y = q.pop(0)
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nx, ny = x + dx, y + dy
            if N > nx >= 0 and M > ny >= 0 and pan[nx][ny] == ".":
                q.append((nx, ny))
                pan[nx][ny] = "#"
                cnt += 1
    return cnt


for _ in range(int(input())):
    N, M = map(int, input().split())
    pan = [list(input()) for _ in range(N)]
   
    sections = 0
    spaces = 0
    for n in range(N):
        for m in range(M):
            if pan[n][m] == ".":
                sections += 1
                spaces += bfs(n, m)
    if sections == 1:
        sc = "section"
    else:
        sc = "sections"
    if spaces == 1:
        sp = "space"
    else:
        sp = "spaces"
    print(f"{sections} {sc}, {spaces} {sp}")
