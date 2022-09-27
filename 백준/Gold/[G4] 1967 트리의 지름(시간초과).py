def dfs(n):
    global co
    if Tr[n] == [] and s and co:
        s.append(n)
        res.append([tuple(s), co])
        s.pop()
        return

    visited[n] = 1
    for w in Tr[n]:
        if not visited[w[0]]:
            co += w[1]
            s.append(n)
            dfs(w[0])
            s.pop()
            co -= w[1]


def combi():
    global counts
    if len(q) == 2 and q[0][0][0] != q[1][0][0]:
        return

    # print(q)
    if len(q) == 1:
        ans.append(counts)

    if len(q) == 2:
        if q[0][0][1] != q[1][0][1]:
            ans.append(counts)
            return
        else:
            return



    for i in range(len(res)):
        if re_vis[i] == 1:
            continue
        re_vis[i] = 1
        counts += res[i][1]
        q.append(res[i])
        combi()
        q.pop()
        counts -= res[i][1]
        re_vis[i] = 0


V = int(input())
Tr = [[] for _ in range(V+1)]

if V == 1:
    print(0)
    quit()

for _ in range(V-1):
    a, b, c = map(int, input().split())
    Tr[a] += [[b, c]]


res = []
for n in range(1, V+1):
    co = 0
    s = []
    visited = [0 for _ in range(V+1)]
    dfs(n)

ans = []
q = []
counts = 0
re_vis = [0 for _ in range(len(res))]
combi()

print(max(ans))