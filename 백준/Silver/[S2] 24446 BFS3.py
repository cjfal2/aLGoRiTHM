from collections import deque
import sys
input = sys.stdin.readline

N, M, R = map(int, input().strip().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().strip().split())
    G[a] += [b]
    G[b] += [a]
for j in range(1, N+1):
    G[j].sort()

visited = [0 for _ in range(N+1)]
visited[R] = 1
q = deque()
q.append(R)
temp2 = [-1 for _ in range(N+1)]
temp2[R] = 0
i = 0
while q:
    i += 1
    for _ in range(len(q)):
        t = q.popleft()
        for r in G[t]:
            if not visited[r]:
                visited[r] = 1
                temp2[r] = i
                q.append(r)

for z in range(1, N+1):
    print(temp2[z])
