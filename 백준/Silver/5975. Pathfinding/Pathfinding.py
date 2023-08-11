N, M = map(int, input().split())

G = [[] for _ in range(N + 1)]

for i in range(1, N + 1):
    G[i] = list(map(int, input().split()))

visited = [-1] * (N + 1)
visited[M] = 0

q = [M]
while q:
    x = q.pop(0)
    for i in range(1, N + 1):
        if G[x][i-1] == 1 and visited[i] == -1:
            visited[i] = visited[x] + 1
            q.append(i)

answer = [[] for _ in range(max(visited) + 1)]

for i in range(1, N + 1):
    if visited[i] != -1:
        answer[visited[i]].append(i)

for a in answer:
    if a:
        print(*a)
