import sys
input = sys.stdin.readline

def find(a):
    if arr[a]!=a:
        arr[a]=find(arr[a])
    return arr[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        arr[a] = b
    else:
        arr[b] = a

V, E = map(int, input().strip().split())
arr = [i for i in range(V + 1)]
edge = []
for _ in range(E):
    u, v, w = map(int, input().strip().split())
    edge.append((w, u, v))

edge.sort()

p = [i for i in range(V+1)]

cnt = 0
total = 0

for w, u, v in edge:
    if find(u) != find(v):
        cnt = w
        total += w
        union(u, v)
        
print(total - cnt)