import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)


def find(x):
    if rep[x] != x:
        rep[x] = find(rep[x])
    return rep[x]


def union(x, y):
    rep[find(x)] = find(y)


N = int(input().strip())
rep = [n for n in range(N+1)]

for i in range(N-2):
    a, b = map(int, input().strip().split())
    if find(a) != find(b):
        union(a, b)

leaves = [i for i in range(1, N+1) if rep[i] == i]

for leaf in leaves:
    print(leaf, end=" ")
print()
