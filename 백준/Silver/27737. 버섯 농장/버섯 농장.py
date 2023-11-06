N, M, K = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(N)]
res = 0
for n in range(N):
    for m in range(N):
        if pan[n][m] == 0:
            pan[n][m] = 1
            q = [(n, m)]
            temp = 1
            while q:
                x, y = q.pop(0)
                for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                    nx, ny = x + dx, y + dy
                    if N > nx >= 0 and N > ny >= 0 and pan[nx][ny] == 0:
                        pan[nx][ny] = 1
                        q.append((nx, ny))
                        temp += 1
            
            X = temp // K + 1 if temp % K else temp // K
            res += X

if res >= 1:
    if M >= res:
        for n in range(N):
            for m in range(N):
                if pan[n][m] == 0:
                    print("IMPOSSIBLE")
                    quit()
        print("POSSIBLE")
        print(M-res)
    else:
        print("IMPOSSIBLE")
else:
    print("IMPOSSIBLE")