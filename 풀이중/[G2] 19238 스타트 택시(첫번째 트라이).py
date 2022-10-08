def kakao(taxi_x, taxi_y):
    global fuel
    visited = [[False for _ in range(N)] for _ in range(N)]
    for aa, bb in wall:
        visited[aa][bb] = True
    visited[taxi_x][taxi_y] = True
    
    q = [(taxi_x, taxi_y, 0)]
    who = []
    if MAP[taxi_x][taxi_y] != 0 and MAP[taxi_x][taxi_y] != 1:
        who.append((MAP[taxi_x][taxi_y], taxi_x, taxi_y, 0))
    else:
        while q:
            x, y, move = q.pop(0)
            for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                nx = x + dx
                ny = y + dy
                if N > nx >= 0 and N > ny >= 0 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    # 손님이 서있을 경우
                    if MAP[nx][ny] != 0 and MAP[nx][ny] != 1:
                        who.append((MAP[nx][ny], nx, ny, move+1))
                    elif MAP[nx][ny] == 0:
                        q.append((nx, ny, move+1))
    if who:
        who.sort(key=lambda x: (x[3], x[1], x[2]))
        a, b, c, d = who[0]
        return [a, b, c, d]
    else:
        fuel = -1
        return


def start(taxi_x, taxi_y):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for aa, bb in wall:
        visited[aa][bb] = -1
    visited[taxi_x][taxi_y] = 1
    p = [(taxi_x, taxi_y)]
    while p:
        x, y = p.pop(0)
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx = x + dx
            ny = y + dy
            if N > nx >= 0 and N > ny >= 0 and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                if nx == ex and ny == ey:
                    return visited[x][y]
                elif MAP[nx][ny] != 1:
                    p.append((nx, ny))
    return 0


N, M, fuel = map(int, input().split())

MAP = []
wall = []
for i in range(N):
    MAP.append(list(map(int, input().split())))
    for j in range(N):
        if MAP[i][j] == 1:
            wall.append((i, j))

tx, ty = map(int, input().split())
tx -= 1
ty -= 1

call = {}
for _ in range(M):
    a, b, n, m = map(int, input().split())
    MAP[a-1][b-1] = str(a-1)+str(b-1)
    call[str(a-1)+str(b-1)] = (n-1, m-1)

# for v in MAP:
#     print(v)
# print("------------------")

while M:
    taxi = kakao(tx, ty)

    # for v in MAP:
    #     print(v)
    # print()
    # print(taxi, fuel)
    # print("------------------")
    if taxi:
        M -= 1
        whois, rx, ry, m = taxi
        ex, ey = call.get(whois)
        MAP[rx][ry] = 0
        
        if ex==rx and ey==ry:
            continue

        fuel -= m
        if fuel < 0:
            fuel = -1
            break
        
        juhang = start(rx, ry)
        
        if not juhang:
            fuel = -1
            break

        if fuel < juhang:
            fuel = -1
            break
        

        tx = ex
        ty = ey
        fuel = (fuel - juhang) + (juhang*2)
    else:
        break

if not M:
    print(fuel)
else:
    print(-1)