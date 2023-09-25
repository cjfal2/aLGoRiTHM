N, M, x, y, K = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(N)]
move = list(map(int, input().split()))

'''
1. 주사위의 회전 (윗면, 바닥면 고려)
2. 회전시 그거에 맞게 돌리고 D = pan[n][m]
U 출력
'''
dice = {
    "U": 0,
    "D": 0,
    "F": 0,
    "B": 0,
    "L": 0,
    "R": 0,
}

def rotation(direction):
    # 1: 동 / 2: 서 / 3: 북 / 4: 남
    if direction == 1: # 동
        dice["R"], dice["U"], dice["L"], dice["D"] = dice["U"], dice["L"], dice["D"], dice["R"]
    elif direction == 2: # 서
        dice["R"], dice["U"], dice["L"], dice["D"] = dice["D"], dice["R"], dice["U"], dice["L"]
    elif direction == 3: # 북
        dice["B"], dice["U"], dice["F"], dice["D"] = dice["U"], dice["F"], dice["D"], dice["B"]
    elif direction == 4: # 남
        dice["B"], dice["U"], dice["F"], dice["D"] = dice["D"], dice["B"], dice["U"], dice["F"]

dix = [[], [0, 1], [0, -1], [-1, 0], [1, 0]] 


for d in move:
    nx, ny = x + dix[d][0], y + dix[d][1]

    if N > nx >= 0 and M > ny >= 0:
        rotation(d)
        x, y = nx, ny
        if pan[x][y]:
            dice["D"] = pan[x][y]
            pan[x][y] = 0
        else:
            pan[x][y] = dice["D"]
        print(dice["U"])
