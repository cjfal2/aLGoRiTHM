from collections import deque

visited = set()
A, B, S, E = map(int, input().split())
visited.add(S)

q = deque([(S, 0)])
while q:
    x, c = q.popleft()
    if x == E:
        print(c)
        break
    for d in (x*A, x*B, x+A, x+B, x-A, x-B, x+1, x-1):
        if 100000 >= d >= 0 and d not in visited:
            visited.add(d)
            q.append((d, c+1))
