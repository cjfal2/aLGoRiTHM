from copy import deepcopy


news = [[],[-1, 0],[-1, -1],[0, -1],[1, -1],[1, 0],[1, 1],[0, 1],[-1, 1]]

def find(t, pan):
    for x in range(4):
        for y in range(4):
            if pan[x][y][0] == t:
                return x, y, True
    return False, False, False

def dfs(xx, yy, su, ocean):
    global co
    co = max(co, su)
    shark_d = ocean[xx][yy][1]
    ocean[xx][yy][0] = "S"

    for target in range(1, 17):
        fish_x, fish_y, flag = find(target, ocean)
        if flag:
            dix = ocean[fish_x][fish_y][1] - 1
            while 1:
                dix += 1
                if dix > 8:
                    dix = 1
                nx = fish_x + news[dix][0]
                ny = fish_y + news[dix][1]
                if 0 <= nx < 4 and 0 <= ny < 4 and ocean[nx][ny][0] != "S":
                    ocean[fish_x][fish_y][1] = dix
                    ocean[fish_x][fish_y], ocean[nx][ny] = ocean[nx][ny], ocean[fish_x][fish_y]
                    break

    ocean[xx][yy][0] = 0

    dx, dy = news[shark_d][0], news[shark_d][1]
    nx, ny = xx, yy
    for _ in range(3):
        nx += dx
        ny += dy
        if 0 <= nx < 4 and 0 <= ny < 4 and ocean[nx][ny][0]:
            dfs(nx, ny, su+ocean[nx][ny][0], deepcopy(ocean))


sea = [[] for _ in range(4)]
for i in range(4):
    a,aa,b,bb,c,cc,d,dd = map(int, input().split())
    for A,B in [(a,aa),(b,bb),(c,cc),(d,dd)]:
        sea[i].append([A, B])
co = 0

dfs(0, 0, sea[0][0][0], sea)
print(co)