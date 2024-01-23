import sys
input = sys.stdin.readline


def find(a):
    if rep[a] != a:
        rep[a] = find(rep[a])
    return rep[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        rep[a] = b
    else:
        rep[b] = a


N, M = map(int, input().strip().split())
rep = [i for i in range(N + 1)]
edge = []
for _ in range(M):
    u, v, d = map(int, input().strip().split())
    edge.append([d, u, v])
edge.sort()

total = 0
graph = [[] for _ in range(N+1)]
for d, u, v in edge:
    root_u, root_v = find(u), find(v)
    if root_u != root_v:
        union(u, v)
        total += d
        graph[u].append((v, d))
        graph[v].append((u, d))

answer = 0
for z in range(N):
    if len(graph[z]) == 1:
        q = [(z, 0)]
        visited = [0 for _ in range(N+1)]
        visited[z] = 1
        while q:
            x, w = q.pop()
            answer = max(answer, w)
            for y, k in graph[x]:
                if not visited[y]:
                    q.append((y, k + w))
                    visited[y] = 1
print(total)
print(answer)
