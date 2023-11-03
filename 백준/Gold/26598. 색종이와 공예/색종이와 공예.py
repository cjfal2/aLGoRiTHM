N, M = map(int, input().split())
pan = [input() for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

for n in range(N):
    for m in range(M):
        if not visited[n][m]:
            visited[n][m] = 1
            cnt = 1
            last_x, last_y = n, m
            q = [(n, m)]
            what = pan[n][m]
            # print(n, m, what)
            while q:
                x, y = q.pop(0)
                last_x = max(last_x, x+1)
                last_y = max(last_y, y+1)

                for nx, ny in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
                    if N > nx >= 0 and M > ny >= 0 and not visited[nx][ny] and pan[nx][ny] == what:
                        q.append((nx, ny))
                        visited[nx][ny] = 1
                        cnt += 1
            # print(last_x, last_y)
            if abs(last_x - n) * abs(last_y - m) != cnt:
                print("BaboBabo")
                quit()
print("dd")