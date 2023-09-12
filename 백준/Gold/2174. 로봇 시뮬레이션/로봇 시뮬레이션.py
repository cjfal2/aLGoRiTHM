'''
땅 1x1 ~ 100x100 에 로봇 N개
M 개의 명령
L: 로봇이 향하고 있는 방향을 기준으로 왼쪽으로 90도 회전한다.
R: 로봇이 향하고 있는 방향을 기준으로 오른쪽으로 90도 회전한다.
F: 로봇이 향하고 있는 방향을 기준으로 앞으로 한 칸 움직인다.

- 땅에 밖으로 벗어나는 경우: Robot X crashes into the wall
- 로봇에 충돌하는 경우: Robot X crashes into robot Y
- 문제가 없는 경우: OK
'''


def move(robot, command, repeat):
    r = info.get(robot)

    x = r[0]
    y = r[1]
    if command == "F":
        pan[x][y] = 0
        dx = direction[r[2]][0]
        dy = direction[r[2]][1]

        for _ in range(repeat):
            x, y = x + dx, y + dy

            if B > x >= 0 and A > y >= 0:
                if pan[x][y]:
                    return [robot, "robot " + str(pan[x][y])]
            else:
                return [robot, "the wall"]
        r[0] = x
        r[1] = y
        pan[x][y] = robot

    elif command == "L":
        r[2] += repeat
        r[2] %= 4

    elif command == "R":
        r[2] -= repeat
        a = abs(r[2])
        if a % 2:
            a += 2
        r[2] = a % 4

    info[robot] = r
    return [robot, "OK"]


direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 방향
             # 남0     동1     북2     서3
temp = {
    "S": 0,
    "E": 1,
    "N": 2,
    "W": 3
}

A, B = map(int, input().split())  # 가로: A, 세로: B
N, M = map(int, input().split())  # 로봇의 수: N, 명령의 수: M
info = dict()

pan = [[0 for _ in range(A)] for _ in range(B)]  # 판: 시뮬레이션의 판

for i in range(1, N+1):  # 로봇의 번호를 1번 부터 시작
    x, y, d = input().split()  # 초기 로봇 정보
    # 숫자형으로 바꾸고 0,0 기준으로 설정, x랑 y가 생각한거랑 반대로 되어있어서 스왑
    x, y = map(lambda z: int(z) - 1, [y, x])
    pan[x][y] = i  # pan의 (x, y)에 i 로봇이 있다.
    info[i] = [x, y, temp.get(d)]  # i로봇은 (x, y, d) 에 d 방향으로 있다.


for _ in range(M):  # 명령하달
    what, LRF, number = input().split()
    what, number = map(int, [what, number])

    num, result = move(what, LRF, number)
    if result != "OK":
        print(f'Robot {num} crashes into {result}')
        break
else:
    print("OK")
