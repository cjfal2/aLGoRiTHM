"""
6 5 19
1 0 0 0 1 0
1 0 1 0 1 0
1 0 1 0 1 0
1 0 1 0 1 0
1 0 1 0 1 0
0 0 1 0 0 0
1 3
6 1 1 6
1 6 6 2
5 2 2 4
6 5 6 6
4 6 1 2

ans = 59
-----
6 4 50
0 0 0 1 0 0
0 1 1 1 1 0
0 1 0 0 1 0
0 1 0 0 1 0
0 1 1 0 1 0
0 0 0 0 0 0
3 4
1 1 1 6
1 6 6 6
6 6 6 1
6 1 1 1

ans = 75
"""
def kakao(taxi_x, taxi_y):
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
        who.sort(key=lambda x: x[2])
        who.sort(key=lambda x: x[1])
        who.sort(key=lambda x: x[3])
        a, b, c, d = who[0]
        return [a, b, c, d]
    else:
        fuel = -1
        return


def start(taxi_x, taxi_y):
    visited = [[False for _ in range(N)] for _ in range(N)]
    for aa, bb in wall:
        visited[aa][bb] = True
    visited[taxi_x][taxi_y] = True
    p = [(taxi_x, taxi_y)]
    while p:
        x, y = p.pop(0)
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx = x + dx
            ny = y + dy
            if N > nx >= 0 and N > ny >= 0 and not visited[nx][ny]:
                visited[nx][ny] = 1
                if nx == ex and ny == ey:
                    return True
                elif MAP[nx][ny] != 1:
                    p.append((nx, ny))
    return False




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
MAP[tx][ty] = 1

call = {}
for _ in range(M):
    a, b, n, m = map(int, input().split())
    MAP[a-1][b-1] = str(a-1)+str(b-1)
    call[str(a-1)+str(b-1)] = (n-1, m-1)

while M:
    taxi = kakao(tx, ty)

    if taxi:
        M -= 1
        whois, rx, ry, m = taxi
        ex, ey = call.get(whois)
        MAP[rx][ry] = 0
        
        fuel -= m
        if fuel < 0:
            fuel = -1
            break

        distance = abs(ex-rx) + abs(ey-ry)
        if fuel < distance:
            fuel = -1
            break
        
        if not start(rx, ry):
            fuel = -1
            break

        tx = ex
        ty = ey
        fuel = (fuel - distance) + (distance*2)
    else:
        break

print(fuel)