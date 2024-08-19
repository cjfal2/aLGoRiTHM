K, N, M = map(int, input().split())

starts = []
for _ in range(K):
    starts.append(int(input()))

ways = [[] for _ in range(M+1)]
for _ in range(M):
    s, e = map(int, input().split())
    ways[s].append(e)

def bfs(num):
    can_go = set([num])
    q = [num]
    visited = [0 for _ in range(M+1)]
    visited[num] = 1
    while q:
        x = q.pop(0)
        for w in ways[x]:
            if not visited[w]:
                visited[w] = 1
                q.append(w)
                can_go.add(w)
    return can_go

ref = bfs(starts[0])
for s in starts[1:]:
    temp = set()
    for c in bfs(s):
        if c in ref:
            temp.add(c)
    delete = set()
    for r in ref:
        if r not in temp:
            delete.add(r)
    for d in delete:
        ref.remove(d)
print(len(ref))
        
