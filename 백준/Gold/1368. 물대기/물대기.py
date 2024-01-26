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


N = int(input())
edge = []
for i in range(1, N+1):
    n = int(input())
    edge.append([n, 0, i])

for u in range(N):
    temp = list(map(int, input().strip().split()))
    for v in range(u+1, N):
        edge.append([temp[v], u+1, v+1])

edge.sort()

rep = [i for i in range(N + 1)]
total = 0
for d, u, v in edge:
    if find(u) != find(v):
        total += d
        union(u, v)

print(total)
