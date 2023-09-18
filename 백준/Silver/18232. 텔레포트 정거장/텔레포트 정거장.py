import sys
from collections import deque
input = sys.stdin.readline


N, M = map(int, input().strip().split())
S, E = map(int, input().strip().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().strip().split()) 
    G[a].append(b)
    G[b].append(a)

q = deque([S])
visited = [0 for _ in range(N+1)]
visited[S] = 1

while q:
    x = q.popleft()
    if x == E:
        break
    for w in G[x] + [x+1, x-1]:
        if N >= w > 0 and not visited[w]:
            visited[w] = visited[x] + 1
            q.append(w)
print(visited[E]-1)