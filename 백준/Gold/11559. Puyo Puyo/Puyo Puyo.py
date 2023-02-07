from copy import deepcopy


def bfs():
    global cost, end

    def gravity():
        for h in range(12, -1, -1):
            for w in range(6):
                x, y = h, w
                while 1:
                    if 12 > x >= 0 and 6 > y >= 0 and 12 > x+1 >= 0 and L[x][y] != '.' and L[x + 1][y] == '.':
                        L[x + 1][y] = L[x][y]
                        L[x][y] = '.'
                        x += 1
                    else:
                        break


    before = deepcopy(L)

    memo = set()
    for i in range(12):
        for j in range(6):
            if L[i][j] != '.':
                q = [(i, j)]
                num = 1
                temp = []
                temp.append((i, j))
                while q:
                    x, y = q.pop(0)
                    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                        nx, ny = x + dx, y + dy
                        if 12 > nx >= 0 and 6 > ny >= 0 and (nx, ny) not in temp and L[nx][ny] == L[i][j]:
                            q.append((nx, ny))
                            temp.append((nx, ny))
                            num += 1
                if num >= 4:
                    memo.update(temp)
    if memo:
        for n, m in memo:
            L[n][m] = '.'
        cost += 1
        gravity()

        
    if before == L:
        end = False
    


L = [list(input()) for _ in range(12)]
cost = 0
end = True

while end:
    bfs()
    
print(cost)


