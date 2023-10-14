def escape():
    '''
    일단 구슬을 따로 움직인 후에 판단
    '''
    # 하, 우, 상, 좌
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    visited = set() # 움직여본곳 처리
    visited.add((rx_s, ry_s, bx_s, by_s))
    q = [(rx_s, ry_s, bx_s, by_s, 0, "")]

    while q:
        rx, ry, bx, by, cnt, dd = q.pop(0)
        if cnt >= 10:
            return -1, -1
        for d in range(4):
            rx_n, ry_n, move_R = gravity(rx, ry, dx[d], dy[d])
            bx_n, by_n, move_B = gravity(bx, by, dx[d], dy[d])

            if pan[bx_n][by_n] != "O": # 블루가 구멍에 안빠진 경우만!
                if pan[rx_n][ry_n] == "O": # 레드가 구멍에 빠진 경우
                    if d == 0:
                        nd = dd + "D"
                    elif d == 1:
                        nd = dd + "R"
                    elif d == 2:
                        nd = dd + "U"
                    elif d == 3:
                        nd = dd + "L"
                    return cnt + 1, nd

                if rx_n == bx_n and ry_n == by_n: # 두 개가 이동했는데 같은 위치에 있다면
                    # 뒤늦게 도착한 쪽(많은 걸음수)을 하나씩 뒤로 물러나게함 
                    if move_R > move_B:
                        rx_n, ry_n = rx_n - dx[d], ry_n - dy[d]
                    else:
                        bx_n, by_n = bx_n - dx[d], by_n - dy[d]

                if (rx_n, ry_n, bx_n, by_n) not in visited: # 움직여본 곳이라면
                    nd = dd
                    if d == 0:
                        nd = dd + "D"
                    elif d == 1:
                        nd = dd + "R"
                    elif d == 2:
                        nd = dd + "U"
                    elif d == 3:
                        nd = dd + "L"

                    visited.add((rx_n, ry_n, bx_n, by_n))
                    q.append((rx_n, ry_n, bx_n, by_n, cnt + 1, nd))

    return -1, -1


def gravity(x, y, dx, dy):
    # 중력으로 이동 시키기
    # moves: 더 많은 걸음을 한 구슬을 찾아내기 위해
    moves, nx, ny = 0, x, y
    while 1:
        if pan[nx + dx][ny + dy] == '#' or pan[nx][ny] == 'O':
            return nx, ny, moves
        nx += dx
        ny += dy
        moves += 1


N, M = map(int, input().split())
pan = []

for n in range(N):
    t = input()
    pan.append(t)
    for m in range(M):
        if t[m] == 'R':
            rx_s, ry_s = n, m
        if t[m] == 'B':
            bx_s, by_s = n, m

a, b = escape()
if a == -1:
    print(-1)
else:
    print(a)
    print(b)
