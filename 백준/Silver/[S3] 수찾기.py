from collections import deque

A, K = map(int, input().split())
visited = dict()
q = deque()
q.append(A)
visited[A] = 1
while q:
    t = q.popleft()
    if t == K:
        print(visited[t]-1)
        quit()
    for i in [t*2, t+1]:
        if i < K+1 and i not in visited:
            visited[i] = visited[t] + 1
            q.append(i)