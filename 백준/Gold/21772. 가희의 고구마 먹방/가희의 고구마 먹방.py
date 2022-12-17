def DFS(x, y, depth, co):
    global ans
    if pan[x][y] != "#":  # 벽이 아니라면
        if pan[x][y] == 'S': 
            co += 1
        if depth == S:
            ans = max(ans, co)
            return
        else:
            if x-1 >= 0:
                memo = pan[x][y]
                pan[x][y] = '.'
                DFS(x-1, y, depth+1, co)
                pan[x][y] = memo

            if y-1 >= 0:
                memo = pan[x][y]
                pan[x][y] = '.'
                DFS(x, y-1, depth+1, co)
                pan[x][y] = memo

            if x+1 < N:
                memo = pan[x][y]
                pan[x][y] = '.'
                DFS(x+1, y, depth+1, co)
                pan[x][y] = memo

            if y+1 < M:
                memo = pan[x][y]
                pan[x][y] = '.'
                DFS(x, y+1, depth+1, co)
                pan[x][y] = memo

    else:
        return

N, M, S = map(int, input().split())
pan = []
flag = False
for q in range(N):
    ppp = list(input())
    pan.append(ppp)
    if not flag and 'G' in ppp:
        p = -1
        flag = True
        for pp in ppp:
            p += 1
            if pp == 'G':
                gq, gp = q, p
ans = 0
DFS(gq, gp, 0, 0)
print(ans)