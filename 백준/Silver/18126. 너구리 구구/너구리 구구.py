def bfs():
    global MAX
    visited = [0 for _ in range(N+1)]
    visited[1] = 1
    q = [(1, 0)]
    while q:
        t, k = q.pop(0)
        if visited[t]:
            # print(k)
            MAX = max(MAX, k)
        for e, w in G[t]:
            if not visited[e]:
                visited[e] = 1
                q.append((e, k+w))
                # print(k+w)



N = int(input())
G = [[] for _ in range(N+1)]
for number in range(N-1):
    start, end, meter = map(int, input().split())
    G[start].append((end, meter))
    G[end].append((start, meter))
# print(G)
MAX = 0
bfs()
print(MAX)