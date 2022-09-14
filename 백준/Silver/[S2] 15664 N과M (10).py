def dfs(start):
    if len(s) == m:
        print(*s)
        return
    r = 0
    for i in range(start, len(L)):
        if r != L[i] and visited[i] == 0:
            r = L[i]
            visited[i] = 1
            s.append(L[i])
            dfs(i)
            s.pop()
            visited[i] = 0


n, m = map(int, input().split())
L = sorted(map(int, input().split()))
s = []
visited = [0] * (n+1)
dfs(0)
