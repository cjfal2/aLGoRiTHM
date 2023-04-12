import sys
input = sys.stdin.readline

def bfs(idx):
    visited = [0 for _ in range(N+1)]
    visited[idx] = 1
    q = [idx]
    cnt = 1
    while q:
        x = q.pop()
        for w in G[x]:
            if not visited[w]:
                visited[w] = 1
                q.append(w)
                cnt += 1

    global MAX
    MAX = max(MAX, cnt)
    return (idx, cnt)


N, M= map(int, input().strip().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().strip().split())
    G[b].append(a)


temp, MAX = [], 0
for i in range(1, N+1):
    temp.append(bfs(i))
ans = []
for a, b in sorted(temp):
    if b == MAX:
        print(a, end=" ")
