import sys
import heapq
input = sys.stdin.readline


def bfs():
    q = []
    distance = [sys.maxsize for _ in range(N)]
    heapq.heappush(q, (0, 0))
    distance[0] = 0

    while q:
        dist, node = heapq.heappop(q)

        for cost, daum in G[node]:
            if distance[daum] > dist + cost:
                cost += dist
                heapq.heappush(q, [cost, daum])
                distance[daum] = cost

    return distance


N, M = map(int, input().split())
company = [int(input()) for _ in range(N)]

G = [[] for _ in range(N)]
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j] != 0:
            G[i].append([temp[j]+1000001 if company[i] != company[j] else temp[j], j])

dijk = bfs()
print(*divmod(dijk[M], 1000001))
