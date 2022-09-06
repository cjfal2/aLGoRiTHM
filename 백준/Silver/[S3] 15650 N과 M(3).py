def dfs():
    if len(s) == m:
        print(*s)
        return
    for i in range(1, n + 1):
        visited[i] = 1
        s.append(i)
        dfs()
        s.pop()
        visited[i] = 0


n, m = map(int, input().split())
s = []
visited = [0] * (n + 1)
dfs()
