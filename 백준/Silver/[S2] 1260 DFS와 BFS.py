def BFS(G,v,V):
    visited1 = [0 for _ in range(V+1)]
    q = []
    q.append(v)
    visited1[v] = 1
    while q:
        t = q.pop(0)
        bfs.append(t)
        for i in G[t]:
            if visited1[i] == 0:
                q.append(i)
                visited1[i] = visited1[t]+1


def DFS(v):
    global visited, G, N
    visited[v] = 1
    global dfs
    dfs.append(v)
    for w in G[v]:
        if visited[w] == 0:
            DFS(w)


N, M, V = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a] += [b]
    G[a] = sorted(G[a])
    G[b] += [a]
    G[b] = sorted(G[b])
visited = [0]*(N+1)
dfs = []
bfs = []
BFS(G, V, N)
DFS(V)
print(*dfs)
print(*bfs)
