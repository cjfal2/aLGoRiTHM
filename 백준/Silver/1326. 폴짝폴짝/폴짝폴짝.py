N = int(input())
L = list(map(int, input().split()))
a, b = map(int, input().split())
a -= 1
b -= 1
visited = [0 for _ in range(N)]
q = [a]
visited[a] = 1

while q:
    x = q.pop(0)
    if visited[x] and x == b:
        print(visited[x]-1)
        quit()
    for xx in list(range(x, N, L[x])):
        if not visited[xx]:
            visited[xx] = visited[x] + 1
            q.append(xx)
    for xx in list(range(x - L[x], -1, -L[x])):
        if not visited[xx]:
            visited[xx] = visited[x] + 1
            q.append(xx)
print(-1)
