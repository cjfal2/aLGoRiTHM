"""
번호는 1보다 크거나 같고, 16보다 작거나 같은 자연수
두 물고기가 같은 번호를 갖는 경우는 없다
방향은 8가지 방향(상하좌우, 대각선) 중 하나이다.

오늘은 청소년 상어가 이 공간에 들어가 물고기를 먹으려고 한다.
청소년 상어는 (0, 0)에 있는 물고기를 먹고, (0, 0)에 들어가게 된다.
상어의 방향은 (0, 0)에 있던 물고기의 방향과 같다. 이후 물고기가 이동한다.

물고기는 번호가 작은 물고기부터 순서대로 이동한다.
물고기는 한 칸을 이동할 수 있고,
이동할 수 있는 칸은 빈 칸과 다른 물고기가 있는 칸,
이동할 수 없는 칸은 상어가 있거나, 공간의 경계를 넘는 칸이다.
각 물고기는 방향이 이동할 수 있는 칸을 향할 때까지 방향을 45도 반시계 회전시킨다.
만약, 이동할 수 있는 칸이 없으면 이동을 하지 않는다. 그 외의 경우에는 그 칸으로 이동을 한다.
물고기가 다른 물고기가 있는 칸으로 이동할 때는 서로의 위치를 바꾸는 방식으로 이동한다.

물고기의 이동이 모두 끝나면 상어가 이동한다.
상어는 방향에 있는 칸으로 이동할 수 있는데, 한 번에 여러 개의 칸을 이동할 수 있다.
상어가 물고기가 있는 칸으로 이동했다면, 그 칸에 있는 물고기를 먹고, 그 물고기의 방향을 가지게 된다.
이동하는 중에 지나가는 칸에 있는 물고기는 먹지 않는다.
물고기가 없는 칸으로는 이동할 수 없다.
상어가 이동할 수 있는 칸이 없으면 공간에서 벗어나 집으로 간다.
상어가 이동한 후에는 다시 물고기가 이동하며, 이후 이 과정이 계속해서 반복된다.
"""
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

def dfs(xx,yy,dd,su,depth,seacopy):
    global co
    su += seacopy[xx][yy]
    co = max(co, su)
    seacopy[xx][yy] = 'S'

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
                        if 0 <= x+dxx < 4 and 0 <= y+dyy < 4 and seacopy[x+dxx][y+dyy] != "S":
                            seacopy[x][y], seacopy[x+dxx][y+dyy] = seacopy[x+dxx][y+dyy], seacopy[x][y]
                            inform[f] = dix
                            move_list.append(f)
                            break
                        else:
                            dix += 1
                            if dix>8:
                                dix = 1
    seacopy[xx][yy] = 0
    dx, dy = news.get(dd)
    nx, ny = xx, yy
    for _ in range(3):
        nx+=dx
        ny+=dy
        if 0 <= nx < 4 and 0 <= ny < 4 and seacopy[nx][ny] != 0:
            nd = inform.get(seacopy[nx][ny])
            dfs(nx,ny,nd,su,depth+1,deepcopy(seacopy))


sea = [[] for _ in range(4)]
inform = dict()

for i in range(4):
    a,aa,b,bb,c,cc,d,dd = map(int, input().split())
    for A,B in [(a,aa),(b,bb),(c,cc),(d,dd)]:
        sea[i].append(A)
        inform[A] = B

co = 0
dfs(0,0,inform.get(sea[0][0]),sea[0][0],0,sea)
print(co)