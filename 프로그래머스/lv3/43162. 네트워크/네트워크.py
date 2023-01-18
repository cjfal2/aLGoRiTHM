def solution(n, computers):


    def dfs(x, q):
        visited[x] = q
        for w in G[x]:
            if not visited[w]:
                dfs(w, q)


    G = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j]:
                G[i].append(j)

    visited = [0 for _ in range(n)]
    q = 1
    for k in range(n):
        if not visited[k]:
            dfs(k, q)
            q += 1
    return len(set(visited))