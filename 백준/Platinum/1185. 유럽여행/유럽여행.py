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
enter_cost = [float("INF")] + [int(input().strip()) for _ in range(N)]
rep = [i for i in range(N + 1)]
edge = []
for _ in range(M):
    u, v, d = map(int, input().strip().split())
    edge.append([d*2+enter_cost[u]+enter_cost[v], u, v])
edge.sort()

total = 0
for d, u, v in edge:
    if find(u) != find(v):
        union(u, v)
        total += d

print(total+min(enter_cost))
