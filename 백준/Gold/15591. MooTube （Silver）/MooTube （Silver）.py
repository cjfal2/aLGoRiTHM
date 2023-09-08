def bfs(start, k):
    answer = 0
    visited = [0 for _ in range(N+1)]
    visited[start] = 1
    q = []
    for n, v in G[start]:
        visited[n] = 1
        q.append((n, v))
    while q:
        x, c = q.pop(0)
        if c >= k:
            answer += 1
            for w, v in G[x]:
                if not visited[w]:
                    visited[w] = 1
                    q.append((w, min(v, c)))
    print(answer)


N, Q = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, c = map(int, input().split())
    G[a].append((b, c))
    G[b].append((a, c))

for _ in range(Q):
    a, b = map(int, input().split())
    bfs(b, a)