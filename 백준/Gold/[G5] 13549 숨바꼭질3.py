def bfs():
    q = [(N, 0)]
    visited = [0] * (1000000)
    visited[N] = 1

    while q:
        t, m = q.pop(0)
        if t == K :
            return m
        for i, x in [(t*2, True), (t-1, False), (t+1, False)]:
            if not x:
                if 0 <= i < 100002 and not visited[i]:
                    visited[i] = 1
                    q.append((i, m+1))
            else:
                if 0 <= i < 100002 and not visited[i]:
                    visited[i] = 1
                    q.append((i, m))


N, K= map(int,input().split())
print(bfs())