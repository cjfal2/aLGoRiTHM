from itertools import combinations
from copy import deepcopy


def shoot(w):

    def boom(x, y, n):
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx, ny = x, y
            for _ in range(n):
                if H > nx >= 0 and W > ny >= 0:
                    if game[nx][ny] > 1:
                        bomb.append((nx, ny, game[nx][ny]))
                    game[nx][ny] = 0
                    nx += dx
                    ny += dy

    def gravity():
        for h in range(H, -1, -1):
            for w in range(W):
                x, y = h, w
                while 1:
                    if H > x >= 0 and W > y >= 0 and H > x+1 >= 0 and game[x][y] and not game[x + 1][y]:
                        game[x + 1][y] = game[x][y]
                        game[x][y] = 0
                        x += 1
                    else:
                        break

    for h in range(H):
        if game[h][w]:
            bomb = []
            boom(h, w, game[h][w])
            while bomb:
                i, j, num = bomb.pop(0)
                boom(i, j, num)
            break
    gravity()


for tc in range(int(input())):
    N, W, H = map(int, input().split())
    base = [list(map(int, input().split())) for _ in range(H)]
    nums = list(range(W)) * N
    res = []
    for comb in combinations(nums, N):
        game = deepcopy(base)
        for t in comb:
            shoot(t)
        temp = 0
        for i in range(H):
            for j in range(W):
                if game[i][j]:
                    temp += 1
        res.append(temp)
        if temp == 0:
            break
    print(f'#{tc+1} {min(res)}')
