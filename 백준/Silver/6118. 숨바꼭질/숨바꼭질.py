from collections import deque
import sys
input = sys.stdin.readline


N, M = map(int, input().split())

G = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

visited = [-1 for _ in range(N+1)]
visited[1] = 0

q = deque()
q.append(1)


while q:
    x = q.popleft()
    for w in G[x]:
        if visited[w] == -1:
            visited[w] = visited[x] + 1
            q.append(w)

answer_node = 100000
ansewr_distance = max(visited)
answer_numbers = 0
for idx, v in enumerate(visited):
    if v == ansewr_distance:
        if answer_node > idx:
            answer_node = idx
        answer_numbers += 1

print(answer_node, ansewr_distance, answer_numbers)