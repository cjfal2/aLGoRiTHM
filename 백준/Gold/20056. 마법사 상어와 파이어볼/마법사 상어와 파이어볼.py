from copy import deepcopy

news = {
    0: [-1, 0],
    1: [-1, 1],
    2: [0, 1],
    3: [1, 1],
    4: [1, 0],
    5: [1, -1],
    6: [0, -1],
    7: [-1, -1]
}

def jojeol(x, y):
    if x == N:
        x = 0
    elif x == -1:
        x = N-1
    if y == N:
        y = 0
    elif y == -1:
        y = N-1
    return x, y

N, M, K = map(int, input().split())
base = [[[] for _ in range(N)] for _ in range(N)]
pan = [[[] for _ in range(N)] for _ in range(N)]
deca = []
for _ in range(M):
    r,c,m,s,d = list(map(int, input().split()))
    pan[r-1][c-1].append([m,s,d])  # m s d = 질량 이동량 방향
# for v in pan:
#     print(v)
# print("----------------")
for _ in range(K):
    newbase = deepcopy(base)
    
    for i in range(N):
        for j in range(N):
            if pan[i][j]:
                for kk in pan[i][j]:
                    m, s, d = kk
                    dx, dy = news.get(d)
                    nx, ny = i, j
                    for _ in range(s):
                        nx += dx
                        ny += dy
                        nx, ny = jojeol(nx, ny)
                    newbase[nx][ny].append([m,s,d])

    pan = deepcopy(newbase)
    # for v in pan:
    #     print(v)
    # print("--------")
    for h in range(N):
        for w in range(N):
            if len(pan[h][w]) > 1:
                new_m, new_s, check = 0, 0, set()
                for m, s, d in pan[h][w]:
                    new_m += m
                    new_s += s
                    check.add(d%2)
                new_m //= 5
                if new_m == 0:
                    pan[h][w] = []
                    continue
                new_s //= len(pan[h][w])
                if len(list(check)) == 1:
                    dix = [0,2,4,6]
                else:
                    dix = [1,3,5,7]
                pan[h][w] = []
                for z in dix:
                    pan[h][w].append([new_m, new_s, z])
                
    # for v in pan:
    #     print(v)
    # print("---@@@@@-----")
ans = 0
for x in range(N):
    for y in range(N):
        if pan[x][y]:
            for k in pan[x][y]:
                ans += k[0]
print(ans)
