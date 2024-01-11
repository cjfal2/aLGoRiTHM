import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
S = int(input())
gom = set(tuple(map(int, input().split())))


def dfs(x):
    if x in gom:
        return

    if not graph[x]:
        print("yes")
        quit()

    for w in graph[x]:
        dfs(w)


dfs(1)
print("Yes")
