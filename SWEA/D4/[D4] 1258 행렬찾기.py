for tc in range(int(input())):
    N = int(input())
    pan = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    square = []
    for h in range(N):
        for w in range(N):
            if pan[h][w] > 0 and visited[h][w] == 0:
                garo = 1
                sero = 1
                x = h
                y = w
                while 1:
                    x += 1
                    if x < 0 or x >= N or y < 0 or y >= N:
                        break
                    if pan[x][y] == 0:
                        break
                    else:
                        visited[x][y] = 1
                        garo += 1
                x = h
                y = w
                visited[x][y] = 1
                while 1:
                    y += 1
                    if x < 0 or x >= N or y < 0 or y >= N:
                        break
                    if pan[x][y] == 0:
                        break
                    else:
                        visited[x][y] = 1
                        sero += 1
                square.append([garo, sero, garo*sero])

                for z in range(garo):
                    for q in range(sero):
                        visited[h+z][w+q] = 1
    square.sort(key=lambda g: g[0])
    square.sort(key=lambda g: g[2])

    print(f'#{tc+1} {len(square)}', end=' ')
    for i, j, k in square:
        print(i, j, end=' ')
    print()
