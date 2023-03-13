from collections import defaultdict
import sys
sys.setrecursionlimit(10000000)

def dfs(x, d, visited):
    global temp, node
    visited.add(x)
    if temp < d:
        temp, node = d, x

    for w, dix in G[x]:
        if w not in visited:
            dfs(w, d + dix, visited)


G = defaultdict(list)
temp, node = 0, 0

while True:
    try:
        a, b, c = map(int, input().split())
        G[a].append((b, c))
        G[b].append((a, c))
    except:
        break

if G:
    dfs(1, 0, set())
    dfs(node, 0, set())
    print(temp)
    quit()

print(0)
