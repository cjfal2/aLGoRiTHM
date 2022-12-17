import sys
input = sys.stdin.readline

def find_set(x):
    while x != p[x]:
        x = p[x]
    return x

V = int(input().strip())
E = int(input().strip())
edge = []
for _ in range(E):
    u, v, w = map(int, input().strip().split())
    edge.append((w, u, v))

edge.sort()

p = [i for i in range(V+1)]

N = V+1
cnt = 0
total = 0

for w, u, v in edge:
    if find_set(u) != find_set(v):
        cnt += 1
        total += w
        p[find_set(v)] = find_set(u)
        if cnt == V:
            break
        
print(total)