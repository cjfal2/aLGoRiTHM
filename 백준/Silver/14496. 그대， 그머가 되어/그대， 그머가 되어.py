A, B = map(int, input().split())
N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
# print(G)
q= [(A, 0)]
visited = [0 for _ in range(N+1)]
visited[A] = 1
while q:
    x, cnt = q.pop(0)
    # print("x:", x)
    if x == B:
        print(cnt)
        quit()
    for w in G[x]:
        if not visited[w]:
            visited[w] = 1
            q.append((w, cnt+1))
print(-1)