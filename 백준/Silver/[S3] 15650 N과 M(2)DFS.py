def dfs(start):
    if len(s) == m:
        print(*s)
        return
    for i in range(start, n+1):
        if visited[i] == 1:
            continue
        visited[i] = 1
        s.append(i)
        dfs(i)
        s.pop()
        visited[i] = 0


n, m = map(int, input().split())
s = []
visited = [0] * (n+1)
dfs(1)
