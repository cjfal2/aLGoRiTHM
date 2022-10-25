N = int(input())
S, E = map(int,input().split())
M = int(input())
G = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

visited = [-1 for _ in range(N+1)]
q = [S]
visited[S] = 0
while q:
    t = q.pop(0)
    if t == E:
        print(visited[t])
        quit()
    for i in G[t]:
        if visited[i] == -1:
            q.append(i)
            visited[i] = visited[t] + 1
print(-1)