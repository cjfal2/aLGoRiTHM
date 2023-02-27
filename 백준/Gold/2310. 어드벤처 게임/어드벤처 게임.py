def dfs(x, gold):
    global flag
    
    if flag:
        return

    room = info.get(x)

    if room[0] == "T":
        if gold >= room[1]:
            gold -= room[1]
        else:
            return
    else:
        if gold < room[1]:
            gold = room[1]


    visited[x] = 1

    if x == N:
        flag = True
        return

    for w in G[x]:
        if not visited[w]:
            dfs(w, gold)

while 1:
    N = int(input())
    if not N:
        break
    G = [[] for _ in range(N+1)]
    flag = False
    info = dict()
    visited = [0 for _ in range(N+1)]
    
    for i in range(1, N+1):
        a, b, *c = input().split()
        info[i] = (a, int(b))
        for d in c[:-1]:
            G[i].append(int(d))
    
    dfs(1, 0)
    print("Yes") if flag else print("No")

