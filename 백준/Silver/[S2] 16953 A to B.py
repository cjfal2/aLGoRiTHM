def bfs():
    visited = {}
    visited[A] = 1
    q = list()
    q.append(A)
    while q:
        t = q.pop(0)
        for n in [t*2, t*10+1]:
            if n < B:
                visited[n] = visited[t] + 1
                q.append(n)
            if n == B:
                return visited[t] + 1
    return -1


A, B = map(int, input().split())
print(bfs())
