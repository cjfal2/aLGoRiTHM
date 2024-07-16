import sys
from collections import deque

input = sys.stdin.readline

def bfs(graph, n, s, visited):
    q = deque([s])
    while q:
        x = q.popleft()
        for w in graph[x]:
            if not visited[w]:
                q.append(w)
                visited[w] = -visited[x]
            elif visited[w] == visited[x]:
                return "NO"
    return "YES"


for _ in range(int(input().strip())):
    V, E = map(int, input().strip().split())
    G = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().strip().split())
        G[s].append(e)
        G[e].append(s)
    answer = "YES"
    visit = [0 for _ in range(V+1)]
    for s in range(1, V+1):
        if not visit[s]:
            visit[s] = 1
            answer = bfs(G, V, s, visit)
            if answer == "NO":
                break
    print(answer)
