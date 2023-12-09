N = int(input())
G = [[] for _ in range(10000)]
for _ in range(N):
    a, b = map(int, input().split())
    G[a].append(b)


def bfs(s, e):
    visited = [0 for _ in range(10000)]
    visited[s] = 1
    q = [(s, 0)]
    while q:
        x, cnt = q.pop(0)
        if x == e:
            return cnt
        for w in G[x]:
            if not visited[w]:
                if w == e:
                    return cnt
                visited[w] = 1
                q.append((w, cnt+1))
    return -1


while 1:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    temp = bfs(a, b)
    if temp == -1:
        print("No")
    else:
        print("Yes", temp)

