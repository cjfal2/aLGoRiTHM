def dfs(start):
    if len(s) == M:
        print(*s)
        return
    for i in range(start, N):
        if visited[i] == 1:
            continue
        visited[i] = 1
        s.append(L[i])
        dfs(i)
        s.pop()
        visited[i] = 0


N, M = map(int, input().split())
L = sorted(map(int, input().split()))
s = []
visited = [0] * (N+1)
dfs(0)
