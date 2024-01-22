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

t = [999999] + list(map(int, input().split()))
for i in range(1, N+1):
    edge.append([t[i], 0, i])

edge.sort()

total = 0
for d, u, v in edge:
    root_u, root_v = find(u), find(v)
    if root_u != root_v:
        total += d
        union(u, v)

print(total)
