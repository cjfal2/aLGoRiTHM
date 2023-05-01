import sys
input = sys.stdin.readline


def find(a):
    if sep[a] != a:
        sep[a] = find(sep[a])
    return sep[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        sep[a] = b
    else:
        sep[b] = a


while 1:
    V, E = map(int, input().strip().split())
    if V == E == 0:
        break
    sep = [i for i in range(V + 1)]
    edge = []
    original = 0
    for _ in range(E):
        u, v, w = map(int, input().strip().split())
        edge.append((w, u, v))
        original += w
    edge.sort()

    total = 0
    for w, u, v in edge:
        if find(u) != find(v):
            total += w
            union(u, v)

    print(original - total)
