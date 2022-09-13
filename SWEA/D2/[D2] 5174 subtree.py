def dfs(start):
    global co, G, visited
    co += 1
    visited[start] = 1
    for i in G[start]:
        if visited[i] == 0:
            dfs(i)


for tc in range(int(input())):
    e, node = map(int, input().split())
    L = list(map(int, input().split()))
    G = [[] for _ in range(e+2)]
    for idx, n in enumerate(L):
        if idx%2 == 0:
            G[n].append(L[idx+1])
    visited = [0] * (e+2)
    co = 0
    dfs(node)
    print(co)
