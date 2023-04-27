import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)


def find(x):
    if rep[x] != x:
        rep[x] = find(rep[x])
    return rep[x]


def union(x, y):
    rep[find(x)] = find(y)


N, M = map(int, input().strip().split())
rep = [n for n in range(N+1)]

for i in range(M):
    a, b = map(int, input().strip().split())
    if find(a) != find(b):
        union(a, b)
    else:
        print(i+1)
        break
else:
    print(0)
