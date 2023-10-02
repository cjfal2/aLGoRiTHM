def bfs():
    visited = [-1 for _ in range(N+1)]
    visited[1] = 0
    q = [1]
    while q:
        x = q.pop(0)
        for w in G[x]:
            if visited[w] == -1:
                visited[w] = visited[x] + 1
                q.append(w)
    return visited[1:]

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

for _ in range(int(input())):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
    print(*bfs())