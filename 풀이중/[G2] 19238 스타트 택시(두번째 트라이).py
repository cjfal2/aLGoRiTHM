def call(tx, ty):
    global fuel
    visited = [[False for _ in range(N)] for _ in range(N)]
    # 벽 표시
    for aa, bb in wall:
        visited[aa][bb] = True
    # 현 위치 표시
    visited[tx][ty] = True
    
    q = [(tx, ty, 0)]
    who = [] # (손님정보, 행 좌표, 열 좌표, 거리)
    if MAP[tx][ty] != 0 and MAP[tx][ty] != 1: # 제자리에 손님이 있는 경우
        who.append((MAP[tx][ty], tx, ty, 0))
    else:
        while q:
            x, y, move = q.pop(0)
            for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                nx = x + dx
                ny = y + dy
                if N > nx >= 0 and N > ny >= 0 and not visited[nx][ny]:
                    # 일단 방문 처리
                    visited[nx][ny] = True
                    # 최단거리를 넘어갔을 경우
                    if who and move+1 > who[-1][-1]:
                        continue
                    # 손님이 서있을 경우
                    if MAP[nx][ny] != 0 and MAP[nx][ny] != 1:
                        who.append((MAP[nx][ny], nx, ny, move+1))
                    # 손님이 없고 그냥 길일 경우
                    elif MAP[nx][ny] == 0:
                        q.append((nx, ny, move+1))
    if who:
        who.sort(key=lambda x: (x[3], x[1], x[2])) # 요구 순서대로 정렬
        return who[0] # 맨앞에 있는거
    else: # 처음에 벽에 막혀있으면 여기로 오게됨
        fuel = -1
        return


def drive(tx, ty):
    global ex, ey
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for aa, bb in wall:
        visited[aa][bb] = -1
    visited[tx][ty] = 1
    p = [(tx, ty)]
    while p:
        x, y = p.pop(0)
        for dx, dy in [[1, 0], [0, -1], [0, 1], [-1, 0]]:
            nx = x + dx
            ny = y + dy
            if N > nx >= 0 and N > ny >= 0 and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                if nx == ex and ny == ey:
                    return visited[x][y]
                elif MAP[nx][ny] != 1:
                    p.append((nx, ny))
    return 0


N, sonnim, fuel = map(int, input().split())

# 벽의 위치와 MAP의 구조를 한번에 찾아줌
MAP = []
wall = []
for i in range(N):
    MAP.append(list(map(int, input().split())))
    for j in range(N):
        if MAP[i][j] == 1:
            wall.append((i, j))

taxi_x, taxi_y = map(int, input().split())
taxi_x, taxi_y = taxi_x - 1 , taxi_y - 1 # 인덱싱을 위해 1씩 빼줌

# 모든 출발지는 서로 다르며 <- 요거에서 딕셔너리 이용을 생각 (도착지는 같아도 됨)
sonnim_info = dict()
for _ in range(sonnim):
    a,b,c,d = map(int, input().split()) #a,b : 출발좌표, c,d : 도착좌표
    a, b, c, d = a - 1, b - 1, c - 1, d - 1
    MAP[a][b] = str(a)+str(b)
    sonnim_info[str(a)+str(b)] = (c, d)

while sonnim and fuel != -1:
    taxi = call(taxi_x, taxi_y)

    if taxi:
        sonnim -= 1
        whois, rx, ry, m = taxi
        ex, ey = sonnim_info.get(whois) # 손님의 도착지 정보를 가져옴
        MAP[rx][ry] = 0
        
        taxi_x = ex  # 택시위치를 도착지점으로 옮김
        taxi_y = ey
        if ex==rx and ey==ry:  # 손님이 타자마자 내리는 경우 아무행동도 안할것임
            continue

        fuel -= m # 콜거리까지 주행한 거리만큼 빼주는데 연료가 - 가 되면 끝냄
        if fuel < 0:
            fuel = -1
            break
        
        juhang = drive(rx, ry) # 거리 visit으로 주행거리측정
        
        if not juhang: # 콜거리 까지 오고 남은 연료로 주행을 못하는 곳이면
            fuel = -1
            break
        else:
            if fuel < juhang: # 주행할 수는 있는데 거리가 연료보다 크면
                fuel = -1
                break
            else:
                fuel += juhang # 주행가능하면 조건에 맞게 주행만큼 연료 더함
    else:
        break

print(fuel)
