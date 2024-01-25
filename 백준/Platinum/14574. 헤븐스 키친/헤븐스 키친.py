import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

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


def solve(x, y):
    for i in graph[x]:
        if i == y:
            continue
        solve(i, x)
    if y != 0:
        print(y, x)


N = int(input())
chefs = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]

edge = []
for u in range(1, N + 1):
    for v in range(u + 1, N + 1):
        d = (chefs[u][1] + chefs[v][1]) // abs(chefs[u][0] - chefs[v][0])
        edge.append([d, u, v])
edge.sort(reverse=1)


total = 0
rep = [i for i in range(N + 1)]
graph = [[] for _ in range(N+1)]
for d, u, v in edge:
    root_u, root_v = find(u), find(v)
    if root_u != root_v:
        union(u, v)
        total += d
        graph[u].append(v)
        graph[v].append(u)

print(total)
solve(1, 0)
