def bfs():
    visited = [0 for _ in range(N+1)]
    visited[1] = 1
    q = [[1, 0]]
    while q:
        x, cnt = q.pop(0)
        if x == N:
            print(cnt)
            return
        for w in G[x]:
            if visited[w] == 0:
                visited[w] = 1
                q.append([w, cnt+1])
    print(-1)
    return


N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
for i in range(1, M+1):
    a, b = map(int, input().split())
    G[a].append(b)
bfs()