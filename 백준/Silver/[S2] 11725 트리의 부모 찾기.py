def BFS(G, v, V):
    global visited1
    visited1 = [0 for _ in range(V+1)]
    q = list()
    q.append(v)
    visited1[v] = 1
    while q:
        t = q.pop(0)
        for i in G[t]:
            if visited1[i] == 0:
                q.append(i)
                visited1[i] = visited1[t]+1


N = int(input())
J = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    J[b] += [a]
    J[a] += [b]

BFS(J, 1, N)

for i in range(2, len(J)):
    J[i].sort(key=lambda x: visited1[x]) # 먼저 방문한것을 앞으로
    print(J[i][0])
