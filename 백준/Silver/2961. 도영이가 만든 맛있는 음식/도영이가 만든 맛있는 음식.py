def dfs(start):
    global temp
    if h:
        S = 1
        B = 0
        for i in h:
            S *= foods.get(i)[0]
            B += foods.get(i)[1]
        temp = min(temp, abs(S-B))
    for j in range(start, N+1):
        if not visited[j]:
            visited[j] = 1
            h.append(j)
            dfs(j)
            h.pop()
            visited[j] = 0
    


N = int(input())
foods = dict()
for v in range(1, N+1):
    A = tuple(map(int, input().split()))
    foods[v] = A

visited = [0 for _ in range(N+1)]
temp = 9999999999999999
h = []
dfs(1)
print(temp)