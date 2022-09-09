def dfs(start):
    if len(s) == m:
        print(*s)
        return

    for i in range(start, n):
        s.append(L[i])
        dfs(i)
        s.pop()


n, m = map(int, input().split())
L = sorted(map(int, input().split()))
s = []
dfs(0)
