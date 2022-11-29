import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    global MAX
    visited = [0 for _ in range(N+1)]
    visited[1] = 1
    q = deque()
    q.append((1, 0))
    while q:
        t, k = q.popleft()
        if visited[t]:
            MAX = max(MAX, k)
        for e, w in G[t]:
            if not visited[e]:
                visited[e] = 1
                q.append((e, k+w))


N = int(input().strip())
G = [[] for _ in range(N+1)]
for number in range(N-1):
    start, end, meter = map(int, input().strip().split())
    G[start].append((end, meter))
    G[end].append((start, meter))

MAX = 0
bfs()
print(MAX)