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


N, M, K = map(int, input().strip().split())
edge = []

for k in list(map(int, input().split())):
    edge.append([0, 0, k])

for _ in range(M):
    u, v, d = map(int, input().strip().split())
    edge.append([d, u, v])

edge.sort()

rep = [i for i in range(N+1)]
total = 0
for d, u, v in edge:
    if find(u) != find(v):
        total += d
        union(u, v)


print(total)
