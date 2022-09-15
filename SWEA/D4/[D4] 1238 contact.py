import sys


def bfs(start):
    visited = [0] * 101
    q = []
    q.append(start)
    visited[start] = 1
    while q:
        t = q.pop(0)
        for g in G[t]:
            if visited[g] == 0:
                q.append(g)
                visited[g] = visited[t] + 1
    return visited


sys.stdin = open('s1.txt', 'r')
for tc in range(10):
    N, M = map(int, input().split())
    L = list(map(int, input().split()))
    G = [[] for _ in range(101)]
    for i in range(0, len(L), 2):
        G[L[i]].append(L[i+1])
    vis = bfs(M)
    MAX = max(vis)
    result = []
    for i in range(101):
        if vis[i] == MAX:
            result.append(i)
    print(f"#{tc+1} {max(result)}")
