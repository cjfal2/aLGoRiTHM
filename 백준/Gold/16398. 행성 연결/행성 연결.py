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


N = int(input().strip())
rep = [i for i in range(N)]
edge = []

for u in range(N):
    space = list(map(int, input().strip().split()))
    for v in range(u+1, N):
        d = space[v]
        edge.append([d, u, v])
edge.sort()
# print(edge)
total = 0
for d, u, v in edge:
    if find(u) != find(v):
        total += d
        union(u, v)
    # if is_connected(rep):
    #     break

print(total)
