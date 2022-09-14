def dfs():
    if len(s) == m:
        print(*s)
        return
    r = 0
    for i in range(len(L)):
        if r != L[i]:
            r = L[i]
            s.append(L[i])
            dfs()
            s.pop()


n, m = map(int, input().split())
L = sorted(map(int, input().split()))
s = []
dfs()
