def dfs(n=1):
    vis_dfs[n] = 1
    dfs_order.append(n)
    for w in G[n]:
        if vis_dfs[w] == 0:
            dfs(w)


def bfs():
    vis_bfs = [0] * (len(G))
    vis_bfs[1] = 1
    q = [1]
    while q:
        t = q.pop(0)
        bfs_order.append(t)
        for x in G[t]:
            if vis_bfs[x] == 0:
                vis_bfs[x] = 1
                q.append(x)



L = list(map(int, input().split()))
G = [[] for _ in range(len(L)//2)]

for idx, g in enumerate(L):
    if not idx%2:
        G[g] += [L[idx+1]]
        G[L[idx+1]] += [g]
        

# print(G)
# [[], [2, 3], [4, 5], [7], [6], [6], [7], []]
# [0     1       2     3     4   5    6    7]

vis_dfs = [0] * (len(G))
dfs_order = []
dfs()
print("dfs", *dfs_order)

bfs_order = []
bfs()
print("bfs", *bfs_order)