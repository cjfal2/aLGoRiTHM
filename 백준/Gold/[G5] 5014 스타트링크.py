F, S, G, U, D = map(int, input().split())
visited = dict()
visited[S] = 1
q = [S]
while q:
    t = q.pop(0)
    if 0 < t <= F:
        if t == G:
            print(visited[t]-1)
            quit()
        for i in [t+U, t-D]:
            if i not in visited:
                visited[i] = visited[t] + 1
                q.append(i)
print("use the stairs")