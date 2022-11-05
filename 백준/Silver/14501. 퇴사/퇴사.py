def dfs(start, e):
    global ans, co
    if start == len(L):
        return
    for i in range(start, len(L)):
        if L[i][0] > e:
            co += L[i][2]
            ans = max(co, ans)
            dfs(i, L[i][1])
            co -= L[i][2]


N = int(input())
L = []
for i in range(1, N+1):
    x, y = map(int, input().split())
    if i+x-1 < N+1:
        L.append([i, i+x-1, y])
# for v in L:
#     print(v)
visited = [0 for _ in range(len(L))]
ans = 0
co = 0
if L:
    dfs(0,0)
print(ans)


