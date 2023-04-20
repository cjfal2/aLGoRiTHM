import sys
input = sys.stdin.readline
from collections import deque

N, M, K, X = map(int, input().strip().split()) # 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
graph = [[] for _ in range(N+1)]
ans = []
for _ in range(M):
    a, b = map(int, input().strip().split())
    graph[a].append(b)

visited = [0 for _ in range(N+1)]
visited[X] = 1
q = deque([X])
while q:
    w = q.popleft()
    for p in graph[w]:
        if not visited[p]:
            q.append(p)
            visited[p] = visited[w] + 1
            if visited[p]-1 == K:
                ans.append(p)

if ans:
    for a in sorted(ans):
        print(a)
else:
    print(-1)
