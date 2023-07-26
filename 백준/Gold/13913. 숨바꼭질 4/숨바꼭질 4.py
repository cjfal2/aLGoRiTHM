from collections import deque

def bfs():
    q = deque([(N, 0)])
    visited = [False] * 100001
    visited[N] = True

    while q:
        t, m = q.popleft()
        if t == K:
            path = [t]
            while t != N:
                t, prev = visited[t]
                path.append(t)
            return path[::-1], m

        for i in [t+1, t-1, t*2]:
            if 0 <= i < 100001 and not visited[i]:
                visited[i] = (t, m)
                q.append((i, m+1))

N, K = map(int, input().split())
a, b = bfs()
print(b)
print(*a)
