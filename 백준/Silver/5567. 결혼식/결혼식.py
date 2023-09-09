n = int(input())
G = [[] for _ in range(n+1)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

visited = [0 for _ in range(n+1)]
visited[1] = 1
q = [(1, 0)]
answer = 0
while q:
    x, d = q.pop(0)
    if d >= 2:
        continue

    for w in G[x]:
        if not visited[w]:
            visited[w] = 1
            q.append((w, d+1))
            answer += 1
print(answer)