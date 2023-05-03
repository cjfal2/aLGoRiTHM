from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)


# DFS 함수
def dfs(G, x, visited, s):
    if x not in visited:
        visited.add(x)
        for neighbor in G[x]:
            dfs(G, neighbor, visited, s)
        s.append(x)


# DFS를 사용한 위상 정렬 함수
def topological_sort_dfs(G):
    visited = set()
    s = []
    for x in list(G):
        if x not in visited:
            dfs(G, x, visited, s)
    return s[::-1]


N, M = map(int, input().strip().split())
G = defaultdict(list)
memo = set(list(range(1, N+1)))
for _ in range(M):
    u, v = map(int, input().strip().split())
    G[u].append(v)
    if u in memo:
        memo.remove(u)
    if v in memo:
        memo.remove(v)

result = topological_sort_dfs(G)
print(*(result+list(memo)))
