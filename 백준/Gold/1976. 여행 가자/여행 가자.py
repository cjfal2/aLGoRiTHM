def dfs(x):
    visited[x] = 1
    for w in G[x]:
        if not visited[w]:
            dfs(w)

N, M = int(input()), int(input())
G = [set() for _ in range(N+1)]
for i in range(1, N+1):
    j = 0
    for num in list(map(int, input().split())):
        j += 1
        if i != j and num:
            G[i].add(j)
            G[j].add(i)

road = list(map(int, input().split()))
visited = [0 for _ in range(N+1)]
dfs(road[0])

for num in set(road):
    if not visited[num]:
        print("NO")
        quit()
print("YES")