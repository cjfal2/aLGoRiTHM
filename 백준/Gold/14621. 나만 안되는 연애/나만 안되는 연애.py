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


def is_connected(parent):
    root = find(1)
    for i in range(1, len(parent)):
        if find(i) != root:
            return False
    return True


V, E = map(int, input().strip().split())
gender = [''] + list(input().strip().split())
rep = [i for i in range(V + 1)]
edge = []
for _ in range(E):
    u, v, d = map(int, input().strip().split())
    edge.append([d, u, v])
edge.sort()


total = 0
for d, u, v in edge:
    if gender[u] == gender[v]:
        continue
    if find(u) != find(v):
        total += d
        union(u, v)

if is_connected(rep):
    print(total)
else:
    print(-1)
