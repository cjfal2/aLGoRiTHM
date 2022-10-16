import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(x):
    global i, visited
    i += 1
    visited[x] = i
    for w in G[x]:
        if not visited[w]:
            dfs(w)

N, M, R = map(int, input().strip().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().strip().split())
    G[a] += [b]
    G[b] += [a]
for j in range(1, N+1):
    G[j].sort()

visited = [0 for _ in range(N+1)]
i = 0
dfs(R)

for z in range(1, N+1):
    print(visited[z])
