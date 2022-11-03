def call_taxi(tx, ty):
    if MAP[tx][ty] == 2:
        return tx, ty, 0

    who = []
    MIN = 100
    visited = [[0] * N for _ in range(N)]
    visited[tx][ty] = 1
    q = []
    q.append([tx, ty])
    while q:
        i, j = q.pop(0)
        if MIN < visited[i][j]: # 거리가 넘어가면 와일 종료
            break
        for di, dj in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and MAP[ni][nj] != 1:
                if MAP[ni][nj] == 2:
                    who.append([ni, nj])
                    MIN = visited[i][j]
                    q.append([ni, nj])
                    visited[ni][nj] = visited[i][j] + 1
                else:
                    q.append([ni, nj])
                    visited[ni][nj] = visited[i][j] + 1
    if who:
        who.sort(key = lambda x: (x[0], x[1]))
        return who[0] + [MIN] # 택시x, 택시y, 이동거리
    return -1, -1, -1


def drive(rx, ry, ex, ey):
    visited = [[0] * N for _ in range(N)]
    visited[rx][ry] = 1
    q = []
    q.append([rx, ry])
    while q:
        x, y = q.pop(0)
        for di, dy in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
            nx, ny = x + di, y + dy
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and MAP[nx][ny] != 1:
                if nx == ex and ny == ey:
                    return visited[x][y]
                else:
                    q.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1
    return -1


N, M, fuel = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
tx, ty = map(int, input().split())
tx, ty = tx - 1, ty - 1
sonnim = []
for _ in range(M):
    rx, ry, ex, ey = map(int, input().split())
    MAP[rx - 1][ry - 1] = 2 # 손님위치는 2
    sonnim.append([rx - 1, ry - 1, ex - 1, ey - 1])

while M:
    rx, ry, m = call_taxi(tx, ty)
    MAP[rx][ry] = 0  # 손님 지우기
    if fuel > m and m != -1:
        fuel -= m
    else:
        fuel = -1
        break

    for i in range(M):
        if sonnim[i][:2] == [rx, ry]:
            ex, ey = sonnim[i][2:]
            sonnim.pop(i)
            M -= 1
            break

    juhang = drive(rx, ry, ex, ey)
    if fuel >= juhang and juhang != -1:
        fuel -= juhang
    else:
        fuel = -1
        break

    tx, ty = ex, ey
    fuel += juhang * 2

print(fuel)