import sys
import heapq


def dijk(start, end):
    q = []
    heapq.heappush(q, (0, start))  # 시작 노드 정보 우선순위 큐에 삽입
    distance = [BIG for _ in range(N+1)]  # 거리 저장소
    distance[start] = 0  # 시작 노드 -> 시작노드 거리 기록
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue

        if node == end:
            break

        for daum, cost in G[node]:
            co = dist + cost
            if co < distance[daum]:
                distance[daum] = co
                heapq.heappush(q, (co, daum))

    return distance[end]


N, M = map(int, input().split())
G = [[] for _ in range(N+1)]  # 그라프 생성
for _ in range(M):  # 그래프 갱신
    s, e, g = map(int, input().split())
    G[s].append((e, g))
    G[e].append((s, g))

BIG = sys.maxsize
X, Y = map(int, input().split())
one = [dijk(1, X)]
one.append(dijk(X, Y))
one.append(dijk(Y, N))

two = [dijk(1, Y)]
two.append(dijk(Y, X))
two.append(dijk(X, N))

if BIG in one or BIG in two:
    print(-1)
else:
    print(min(sum(one), sum(two)))
