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
temp1 = [0 for _ in range(N+1)]
temp1[R] = 1
temp2 = [-1 for _ in range(N+1)]
temp2[R] = 0
i = 0
j = 1
while q:
    i += 1
    for _ in range(len(q)):
        t = q.popleft()
        for r in G[t]:
            if not visited[r]:
                visited[r] = 1
                j += 1
                temp1[r] = j
                temp2[r] = i
                q.append(r)

ans = 0
for z in range(1, N+1):
    ans += temp1[z]*temp2[z]
print(ans)
