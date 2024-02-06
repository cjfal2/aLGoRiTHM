import sys
import heapq


def dijk(start):
    q = []
    heapq.heappush(q, (0, start))  # 시작 노드 정보 우선순위 큐에 삽입
    distance = [BIG for _ in range(N+1)]  # 거리 저장소
    distance[start] = 0  # 시작 노드 -> 시작노드 거리 기록
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue

        for daum, cost in G[node]:
            co = dist + cost
            if co < distance[daum]:
                distance[daum] = co
                heapq.heappush(q, (co, daum))

    return distance


N, M, X = map(int, input().split())
BIG = sys.maxsize
G = [[] for _ in range(N+1)]  # 그라프 생성
for _ in range(M):  # 그래프 갱신
    s, e, g = map(int, input().split())
    G[s].append((e, g))

# 다이크스트라 시작
answer = []
go_home = dijk(X)
for i in range(1, N+1):
    go_party = dijk(i)
    answer.append(go_party[X] + go_home[i])

print(max(answer))
