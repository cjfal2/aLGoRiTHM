for tc in range(int(input())):
    V, E = map(int, input().split())
    G = [[] for _ in range(V+1)]

    for _ in range(E):
        u, v = map(int, input().split())
        G[u] += [v]
        G[v] += [u]

    visited = [0 for _ in range(V+1)]

    q = [1]
    visited[1] = 1
    for _ in range(2):
        for _ in range(len(q)):
            t = q.pop(0)
            for k in G[t]:
                if not visited[k]:
                    visited[k] = 1
                    q.append(k)

    print(f'#{tc+1} {sum(visited)-1}')