def bfs():
    q = [(N, 0)]
    visited = dict()
    visited[N] = [N]

    while q:
        t, m = q.pop(0)
        if t == K :
            return visited[t], m
        for i in [t+1,t-1,t*2]:
            if 0 <= i < 100001 and i not in visited:
                visited[i] = visited[t]+[i]
                q.append((i, m+1))


N, K= map(int,input().split())
a, b = bfs()
print(b)
print(*a)