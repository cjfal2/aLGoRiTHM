def dfs():
    if len(s) == m:
        print(*s)
        return

    for i in L:
        if i in s:
            continue
        s.append(i)
        dfs()
        s.pop()


n, m = map(int, input().split())
L = sorted(map(int, input().split()))
s = []
dfs()
