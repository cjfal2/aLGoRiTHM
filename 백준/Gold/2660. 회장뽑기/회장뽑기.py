from collections import deque
import sys

input = sys.stdin.readline


def bfs(n):
    visited = [0 for _ in range(N+1)]
    visited[n] = 1
    q = deque([n])
    
    while q:
        x = q.popleft()
        for w in G[x]:
            if not visited[w]:
                visited[w] = visited[x] + 1
                q.append(w)

    score[n] = max(visited) - 1


N = int(input().strip())
G = [[] for _ in range(N + 1)]
score = [sys.maxsize for _ in range(N+1)]


while 1:
    a, b = map(int, input().split())
    if a == b == -1:
        break
    G[a].append(b)
    G[b].append(a)

for n in range(1, N + 1):
    bfs(n)

answer = min(score)

print(answer, score.count(answer))
temp = []
for n in range(1, N + 1):
    if score[n] == answer:
        temp.append(n)
print(*temp)
