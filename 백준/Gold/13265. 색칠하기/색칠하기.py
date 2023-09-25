import sys
from collections import deque
input = sys.stdin.readline


for _ in range(int(input().strip())):
    def case():
        N, M = map(int, input().strip().split())
        G = [[] for _ in range(N)]
        for _ in range(M):
            a, b = map(lambda x: int(x) - 1, input().strip().split())
            G[a].append(b)
            G[b].append(a)
        visited = [0 for _ in range(N)]

        for k in range(N):
            if visited[k] == 0:
                visited[k] = 1
                q = deque([k])
                while q:
                    x = q.popleft()
                    for w in G[x]:
                        if visited[w] == 0:
                            visited[w] = visited[x] * -1
                            q.append(w)
            else:
                for w in G[k]:
                    if visited[w] == visited[k]:
                        print("impossible")
                        return

        print("possible")
    case()