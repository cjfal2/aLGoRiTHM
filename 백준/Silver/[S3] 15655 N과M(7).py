def dfs():
    if len(s) == M:
        print(*s)
        return
    for i in range(N):
        s.append(L[i])
        dfs()
        s.pop()


N, M = map(int, input().split())
L = sorted(map(int, input().split()))
s = []
dfs()
