import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(x, y):
    global visited
    visited[x] = y
    for w in G[x]:
        if visited[w] == -1:
            dfs(w, y+1)

N, M, R = map(int, input().strip().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().strip().split())
    G[a] += [b]
    G[b] += [a]
for j in range(1, N+1):
    G[j].sort()

visited = [-1 for _ in range(N+1)]
i = 0
dfs(R, i)

for z in range(1, N+1):
    print(visited[z])
