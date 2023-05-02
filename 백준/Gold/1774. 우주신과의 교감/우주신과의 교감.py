from itertools import combinations
from math import sqrt
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


def cal(a, b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)


N, M = map(int, input().strip().split())
rep = [i for i in range(N)]
edge = []
space = []
for i in range(N):
    space.append(list(map(lambda x: int(x)-1, input().strip().split())) + [i])

for u, v in combinations(space, 2):
    d = cal(u, v)
    edge.append([d, u[2], v[2]])
edge.sort()

total = 0
for _ in range(M):
    u, v = map(lambda x: int(x)-1, input().strip().split())
    union(u, v)

for d, u, v in edge:
    if is_connected(rep):
        break
    if find(u) != find(v):
        total += d
        union(u, v)


print(f'{total:.2f}')
