N = int(input())
G = [[] for _ in range(N)]
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if j == i or not temp[j]:
            continue

        G[i].append((temp[j], j))


visited = [0 for _ in range(N)]
answer = 999999999


def dfs(cnt, x, start, vis):
    global answer

    if x == start and vis == N:
        answer = min(answer, cnt)
        return

    if cnt > answer:
        return

    for c, w in G[x]:
        if not visited[w]:
            visited[w] = 1
            dfs(cnt + c, w, start, vis + 1)
            visited[w] = 0


for i in range(N):
    for j in range(len(G[i])):
        dfs(0, i, i, 0)

print(answer)
