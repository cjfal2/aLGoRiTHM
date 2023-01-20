def bfs():
    visited = [-1 for _ in range(n+1)]
    visited[1] = 0
    q = [1]
    while q:
        w = q.pop(0)
        for x in G[w]:
            if visited[x] == -1:
                visited[x] = visited[w] + 1
                q.append(x)
    return visited[1:]

n, m = map(int, input().split()) # n: 도시의 수 m: 도로의 수
G = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    G[a] += [b]
    G[b] += [a]
# print(G, "원래 G")
for _ in range(int(input())):
    c, a, b = map(int, input().split())
    memo = [0]
    if c == 1:
        G[a] += [b]
        G[b] += [a]
    else:
        G[a].pop(G[a].index(b))
        G[b].pop(G[b].index(a))
    # print(G, "바뀐 G")
    print(*bfs())