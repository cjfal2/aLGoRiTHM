def bfs():
    q = [(N, 0)]
    visited = [0] * (100001)
    visited[N] = 1

    while q:
        t, m = q.pop(0)
        if t == K :
            return m
        for i in [t+1,t-1,t*2]:
            if 0 <= i < 100001 and not visited[i]:
                visited[i] = 1
                q.append((i, m+1))


N, K= map(int,input().split())
print(bfs())