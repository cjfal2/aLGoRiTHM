N, S, P = map(int, input().split())
G = [[] for _ in range(N+1)]
for i in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
visited = [0 for _ in range(N+1)]
temp = []

for i in range(1, S+1):
    q = [(i, 0)]
    visited[i] = 1
    while q:
        x, c = q.pop(0)
        for w in G[x]:
            if not visited[w]:
                if w == P:
                    temp.append(c+1)
                else:
                    q.append((w, c+1))
                    visited[w] = 1

temp.sort()
print(N - temp[0] - temp[1] - 1)
