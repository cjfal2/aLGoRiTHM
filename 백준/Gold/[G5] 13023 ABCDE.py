# noinspection PyTypeChecker
def dfs(v, c):
    if c == 0:
        print(v, 'start')
    global visited, G, K
    print(v)
    if c == 4:
        K = 1
        return K
    visited[v] = 1
    for k in G[v]:
        if visited[k] == 0:
            dfs(k, c+1)
    visited[v] = 0
    print("-------------")

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a] += [b]
    G[b] += [a]
K = 0
for i in range(N):
    if not K:
        visited = [0] * N
        co = 0
        dfs(i, co)
        print("#############")
print(K)
