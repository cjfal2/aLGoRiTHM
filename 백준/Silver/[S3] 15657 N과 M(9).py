def dfs():
    if len(s) == m:
        print(*s)
        return
    r = 0
    for i in range(len(L)):
        if visited[i] == 0 and r != L[i]:
            visited[i] = 1
            r = L[i]
            s.append(L[i])
            dfs()
            s.pop()
            visited[i] = 0


n, m = map(int, input().split())
L = sorted(map(int, input().split()))
s = []
q = []
visited = [0] * (n+1)
dfs()
