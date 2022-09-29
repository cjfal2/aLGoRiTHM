def dfs(start):
    global ans
    if len(s) == N//2:
        res_num = []
        for x in list(range(N)):
            if x not in s:
                res_num.append(x)
        Q1 = 0
        Q2 = 0
        for x in s:
            for y in s:
                Q1 += L[x][y]
        for x in res_num:
            for y in res_num:
                Q2 += L[x][y]
        h = abs(Q1-Q2)
        if ans > h:
            ans = h
        return

    for i in range(start, N):
        if i not in s:
            s.append(i)
            dfs(i)
            s.pop()


N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]
s = []
ans = 999999
dfs(0)
print(ans)