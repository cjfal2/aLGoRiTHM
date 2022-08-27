def gase(wall, x1, y1):
    news = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    co = wall[x1][y1]
    for i, j in news:
        x = x1
        y = y1
        z = 1
        while 1:
            x += i
            y += j
            if 0 <= x < N and 0 <= y < N:
                if z == M:
                    break
                co+=wall[x][y]
                z += 1
            else:
                break
    MAX.append(co)

def degak(wall, x1, y1):
    news = [[-1, 1], [1, 1], [1, -1], [-1, -1]]
    co = wall[x1][y1]
    for i, j in news:
        x = x1
        y = y1
        z = 1
        while 1:
            x += i
            y += j
            if 0 <= x < N and 0 <= y < N:
                if z == M:
                    break
                co+=wall[x][y]
                z += 1
            else:
                break
    MAX.append(co)

for tc in range(int(input())):
    N, M = map(int, input().split())
    wall = [list(map(int, input().split())) for _ in range(N)]
    MAX = []
    for x in range(N):
        for y in range(N):
            gase(wall, x, y)
            degak(wall, x, y)
    print(f'#{tc+1} {max(MAX)}')