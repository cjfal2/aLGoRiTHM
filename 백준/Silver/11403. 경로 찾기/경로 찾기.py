N = int(input())

G = [[] for _ in range(N)]
pan = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if pan[i][j]:
            G[i].append(j)


def dfs(first, x, y, depth):
    global flag
    if x == y and depth:
        flag = 1
        return
    if first != x:
        visited[x] = 1
    for w in G[x]:
        if not visited[w]:
            dfs(first, w, y, depth+1)


answer = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        flag = 0
        visited = [0 for _ in range(N)]
        dfs(i, i, j, 0)
        if flag:
            answer[i][j] = 1

for v in answer:
    print(*v)