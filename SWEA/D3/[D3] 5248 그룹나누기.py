def dfs(n):
    global co
    if visited[n] == 1:
        co = 0
        return

    visited[n] = 1
    co += 1
    
    for w in G[n]:
        if visited[w] == 0:
            dfs(w)


for tc in range(int(input())):
    N, M = map(int, input().split())
    L = list(map(int, input().split()))
    
    G = [[] for _ in range(N+1)]
    for idx, g in enumerate(L):
        if not idx%2:
            G[g] += [L[idx+1]]
            G[L[idx+1]] += [g]

    visited = [0] * (N+1)
    ans = []
    for i in list(range(1, N+1)):
        co = 0
        dfs(i)
        if co > 0:
            ans.append(co)

    print(f'#{tc+1} {len(ans)}')