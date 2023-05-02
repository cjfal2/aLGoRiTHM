import sys
input = sys.stdin.readline


def find(a):
    if rep[a] != a:
        rep[a] = find(rep[a])
    return rep[a]


def union(a, b):
    a = find(a)
    b = find(b)
    # c = min(a, b)
    # rep[a] = c
    # rep[b] = c
    if a > b:
        rep[a] = b
    else:
        rep[b] = a

V, E = map(int, input().strip().split())
rep = [i for i in range(V + 1)]
edge = []
co = 0
for _ in range(E):
    u, v, w = map(int, input().strip().split())
    edge.append([w, u, v])
    co += w
edge.sort()


total = 0
for w, u, v in edge:
    if find(u) != find(v):
        total += w
        union(u, v)

temp = list(set(rep[1:]))

def is_connected(parent):
    root = find(1)
    for i in range(1, len(parent)):
        if find(i) != root:
            return False
    return True

if is_connected(rep):


    print(co - total)
else:
    print(-1)