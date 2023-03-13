N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, c = map(int, input().split())
    G[a].append((b, c))
    G[b].append((a, c))

for _ in range(M):
    start, end = map(int, input().split())
    visited = [0 for _ in range(N+1)]
    visited[start] = 1
    q = [(start, 0)]
    while q:
        x, d = q.pop(0)
        if x == end:
            print(d)
            break
        for w, dix in G[x]:
            if not visited[w]:
                visited[w] = 1
                q.append((w, d + dix))
