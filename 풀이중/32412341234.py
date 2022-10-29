# 청소년 상어 - BOJ 19236
# DFS+구현
from copy import deepcopy

news = {
    1: [-1, 0],
    2: [-1, -1],
    3: [0, -1],
    4: [1, -1],
    5: [1, 0],
    6: [1, 1],
    7: [0, 1],
    8: [-1, 1],
}

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

sea = [[] for _ in range(4)]

inform = dict()

for i in range(4):
    a,aa,b,bb,c,cc,d,dd = map(int, input().split())
    for A,B in [(a,aa),(b,bb),(c,cc),(d,dd)]:
        sea[i].append(A)
        inform[A] = B
co = 0

def dfs(sx, sy, su, dd, seacopy):
    global co
    su += seacopy[sx][sy]
    co = max(co, su)

    seacopy[sx][sy] = 0

    # 물고기 움직임
    for f in range(1,17):
        move_list = []
        for x in range(4):
            if f in move_list:
                break
            for y in range(4):
                if f in move_list:
                    break
                if seacopy[x][y] == f and f not in move_list:
                    dix = inform.get(f)
                    while 1:
                        dxx, dyy = news.get(dix)
                        if 0 <= x+dxx < 4 and 0 <= y+dyy < 4:
                            seacopy[x][y], seacopy[x+dxx][y+dyy] = seacopy[x+dxx][y+dyy], seacopy[x][y]
                            inform[f] = dix
                            move_list.append(f)
                            break
                        else:
                            dix += 1
                            if dix>8:
                                dix = 1

    # 상어 먹음
    dx, dy = news.get(dd)
    for i in range(1, 5):
        nx = sx + dx*i
        ny = sy + dy*i
        if (0<= nx < 4 and 0<= ny < 4) and sea[nx][ny] > 0:
            dfs(nx, ny, su, inform.get(seacopy[nx][ny]),deepcopy(seacopy))

dfs(0, 0, 0, inform.get(sea[0][0]),sea)
print(co)