import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(x, y):
    global visited, i, aaa
    i += 1
    visited[x] = 1
    aaa += (y*i)
    for w in G[x]:
        if not visited[w]:
            dfs(w, y+1)

N, M, R = map(int, input().strip().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().strip().split())
    G[a] += [b]
    G[b] += [a]
for k in range(1, N+1):
    G[k].sort()

visited = [0 for _ in range(N+1)]
i = 0
aaa = 0
dfs(R, 0)
print(aaa)
