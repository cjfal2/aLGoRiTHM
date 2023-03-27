N, M = map(int, input().split())
pan = []
wolves = []
for n in range(N):
    a = input().replace(".", "P")
    for m in range(M):
        if a[m] == 'W':
            wolves.append((n, m))
    pan.append(list(a))

# for v in pan:
#     print(v)

visited = [[0 for _ in range(M)] for _ in range(N)]
for x, y in wolves:
    visited[x][y] = 1
cnt = 0
while wolves:
    cnt += 1
    if cnt > 100000:
        break
    x, y = wolves.pop(0)
    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
        nx, ny = x + dx, y + dy
        if not visited[nx][ny] and pan[nx][ny] in '+P':
            if pan[nx][ny] == 'P':
                visited[nx][ny] = 1
                wolves.append((nx, ny))
                pan[nx][ny] = '.'
            else:
                while 1:
                    nx += dx
                    ny += dy
                
                    if pan[nx][ny] in 'P':
                        wolves.append((nx, ny))
                        pan[nx][ny] = '.'
                        visited[nx][ny] = 1
                        break
                    elif pan[nx][ny] == "#":
                        wolves.append((nx - dx, ny - dy))
                        visited[nx - dx][ny - dy] = 1
                        break



for v in pan:
    print(*v, sep="")

                    

                        
