from itertools import combinations

N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]

ans = 9999999999
for a in list(combinations(list(range(N)), N//2)):
    res_num = []
    for x in list(range(N)):
        if x not in a:
            res_num.append(x)
    Q1 = 0
    Q2 = 0
    for x in a:
        for y in a:
            Q1 += L[x][y]
    for x in res_num:
        for y in res_num:
            Q2 += L[x][y]
    h = abs(Q1-Q2)
    if ans > h:
        ans = h
print(ans)