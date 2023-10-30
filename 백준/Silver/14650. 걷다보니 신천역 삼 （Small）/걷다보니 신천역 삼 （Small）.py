def dfs():
    global c

    if len(s) == N:
        if s[0] != "0" and not sum(map(int, s)) % 3:
            c += 1
        return

    for n in "012":
        s.append(n)
        dfs()
        s.pop()


N, s, c = int(input()), [], 0
dfs()
print(c)
