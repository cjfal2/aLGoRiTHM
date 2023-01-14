def solution(m, n, board):

    def pang(m, n):
        f = False
        memo = set()
        for i in range(m-1):
            for j in range(n-1):
                if pan[i][j] and pan[i][j] == pan[i][j+1] == pan[i+1][j+1] == pan[i+1][j]:
                    memo.add((i, j))
                    memo.add((i+1, j))
                    memo.add((i, j+1))
                    memo.add((i+1, j+1))
                    f = True
                
        return list(memo), f
    

    def gravity(m, n):
        for h in range(m, -1, -1):
            for w in range(n):
                x, y = h, w
                while 1:
                    if m > x >= 0 and n > y >= 0 and m > x+1 >= 0 and pan[x][y] and not pan[x+1][y]:
                        pan[x+1][y] = pan[x][y]
                        pan[x][y] = 0
                        x += 1
                    else:
                        break

    answer = 0
    pan = []
    for brd in board:
        p = []
        for w in brd:
            p.append(w)
        pan.append(p)

    flag = True
    while flag:
        mem, flag = pang(m, n)
        for x, y in mem:
            pan[x][y] = 0
            answer += 1
        gravity(m, n)

    return answer