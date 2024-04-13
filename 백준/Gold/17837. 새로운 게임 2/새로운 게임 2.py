"""
하나의 말 위에 다른 말을 올릴 수 있다.
체스판의 각 칸은 흰색, 빨간색, 파란색 중 하나로 색칠되어있다.

턴 한 번은 1번 말부터 K번 말까지 순서대로 이동시키는 것
한 말이 이동할 때 위에 올려져 있는 말도 함께 이동
말의 이동 방향에 있는 칸에 따라서 말의 이동이 다르며 아래와 같다.
턴이 진행되던 중에 말이 4개 이상 쌓이는 순간 게임이 종료

A번 말이 이동하려는 칸이 흰색인 경우에는 그 칸으로 이동한다.
이동하려는 칸에 말이 이미 있는 경우에는 가장 위에 A번 말을 올려놓는다.

A번 말의 위에 다른 말이 있는 경우에는 A번 말과 위에 있는 모든 말이 이동한다. (A 아래 있는건 무시)

빨간색인 경우에는 이동한 후에 A번 말과 그 위에 있는 모든 말의 쌓여있는 순서를 반대로 바꾼다. (이동한 애들만 reverse후 쌓기)

파란색인 경우에는 A번 말의 이동 방향을 반대로 하고 한 칸 이동한다. 방향을 반대로 바꾼 후에 이동하려는 칸이 파란색인 경우에는 이동하지 않고 가만히 있는다.
(이동하려는 곳이 파랑일 경우 A의 이동방향을 바꿔서 이동해보고 방향을 바꿔도 파랑이면 안움직임)
파랑 == 체스판 밖 (체스판 밖으로 가려고 해도 똑같이 적용)

"""
N, K = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(N)]
units_info = dict()
where_units = dict()

for k in range(1, K+1):
    r, c, d = map(int, input().split())
    r -= 1
    c -= 1
    units_info[k] = [(r, c), d]
    where_units[(r, c)] = [k]

directions = {
    1: (0,  1),  # →
    2: (0, -1),  # ←
    3: (-1, 0),  # ↑
    4: (1,  0),  # ↓
}


end_flag = False
# 게임이 종료되는 턴의 번호를 출력한다. 그 값이 1,000보다 크거나 절대로 게임이 종료되지 않는 경우에는 -1을 출력한다
for turn in range(1, 1001):
    # 움직이는 말의 번호
    for k in range(1, K+1):
        # 이때 움직이는 애들을 전부 체크
        x, y = units_info[k][0]
        temp_move_units = where_units[(x, y)]
        k_idx = temp_move_units.index(k)
        move_units = temp_move_units[k_idx:]
        rest_units = temp_move_units[:k_idx] if temp_move_units[:k_idx] else []
        move_direction = units_info[k][1]
        dx, dy = directions[move_direction]
        # 이동 시켜보기
        nx, ny = x + dx, y + dy
        blue_flag = False
        while 1:
            if N > nx >= 0 and N > ny >= 0:
                if pan[nx][ny] == 2:  # 파란색인 경우 방향을 바꿔야함
                    if not blue_flag:  # 파란색이 첫 번째인 경우
                        nx -= dx
                        ny -= dy
                        if move_direction == 1:
                            move_direction = 2
                        elif move_direction == 2:
                            move_direction = 1
                        elif move_direction == 3:
                            move_direction = 4
                        else:
                            move_direction = 3
                        dx, dy = directions[move_direction]
                        nx += dx
                        ny += dy
                        blue_flag = True
                    else:
                        units_info[k][1] = move_direction
                        break  # 양쪽이 막힌 경우 while 종료
                else:
                    # 이동 가능한 경우
                    if pan[nx][ny] == 1:  # 하얀색인 경우, 그냥 이동
                        # 아니면 빨간색인 경우, move_units를 뒤집어서 이동
                        move_units = move_units[::-1]
                    if where_units.get((nx, ny)):
                        where_units[(nx, ny)].extend(move_units)  # 옮긴 애들 처리
                    else:
                        where_units[(nx, ny)] = move_units

                    if rest_units:
                        where_units[(x, y)] = rest_units  # 남은 애들 처리
                    else:
                        where_units.pop((x, y))
                    for move_unit in move_units:
                        if move_unit == k:
                            units_info[k] = [(nx, ny), move_direction]
                        else:
                            units_info[move_unit][0] = (nx, ny)
                    if len(where_units[(nx, ny)]) >= 4:
                        end_flag = True
                    break  # 이동했으니 while 꺼주기

            else:  # 판을 벗어낫을 경우 방향을 바꿔야함
                if not blue_flag:  # 벽이 첫 번째인 경우
                    nx -= dx
                    ny -= dy
                    if move_direction == 1:
                        move_direction = 2
                    elif move_direction == 2:
                        move_direction = 1
                    elif move_direction == 3:
                        move_direction = 4
                    else:
                        move_direction = 3
                    dx, dy = directions[move_direction]
                    nx += dx
                    ny += dy
                    blue_flag = True
                else:
                    units_info[k][1] = move_direction
                    break  # 파란색이나 넘어가는 부분 이 양쪽일경우
    if end_flag:
        print(turn)
        break
else:
    print(-1)
