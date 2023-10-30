def dfs():
    global c

    if sum(map(int, s)) >= N:
        if sum(map(int, s)) == N:
            c += 1
            if c == K:
                print("+".join(s))
                quit()
        return

    for n in "123":
        s.append(n)
        dfs()
        s.pop()


N, K = map(int, input().split())
s = []
c = 0
dfs()
print(-1)
