import sys
import heapq


def dijk(start, end):
    q = []
    heapq.heappush(q, (0, start, [start]))  # 시작 노드 정보 우선순위 큐에 삽입
    distance = [BIG for _ in range(N+1)]  # 거리 저장소
    distance[start] = 0  # 시작 노드 -> 시작노드 거리 기록
    while q:
        dist, node, road = heapq.heappop(q)
        if distance[node] < dist:
            continue

        if node == end:
            return dist, len(road), road

        for daum, cost in G[node]:
            co = dist + cost
            if co < distance[daum]:
                distance[daum] = co
                heapq.heappush(q, (co, daum, road + [daum]))


N = int(input())
M = int(input())
BIG = sys.maxsize
G = [[] for _ in range(N+1)]  # 그라프 생성
for _ in range(M):  # 그래프 갱신
    s, e, g = map(int, input().split())
    G[s].append((e, g))
s, e = map(int, input().split())

# 다이크스트라 시작
a, b, c = dijk(s, e)
print(a)
print(b)
print(*c)
