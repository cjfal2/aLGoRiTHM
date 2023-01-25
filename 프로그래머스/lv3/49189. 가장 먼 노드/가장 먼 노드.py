def solution(n, edge):
    G = [[] for _ in range(n+1)]
    for a, b in edge:
        G[a].append(b)
        G[b].append(a)
    visited = [0 for _ in range(n+1)]
    visited[1] = 1
    q = [1]
    while q:
        w = q.pop(0)
        for x in G[w]:
            if not visited[x]:
                visited[x] = visited[w] + 1
                q.append(x)
    return visited.count(max(visited))