import sys, heapq


def dijk(start):
    global V, BIG, G, E
    visited = [False for _ in range(V+1)] # 방문 그래프 bool형
    distance = [BIG for _ in range(V+1)] # 거리 저장소
    
    q = []
    heapq.heappush(q, (0, start)) # 시작 노드 정보 우선순위 큐에 삽입
    distance[start] = 0 # 시작 노드 -> 시작노드 거리 기록
    visited[start] = True # 시작 노드 방문 처리
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for daum in G[node]:
            co = distance[node] + daum[1]
            if co < distance[daum[0]]:
                distance[daum[0]] = co
                heapq.heappush(q, (co, daum[0]))

    return distance


V, E = map(int, input().split())
BIG = 9999999999999
G = [[] for _ in range(V+1)] # 그라프 생성
for _ in range(E): # 그래프 갱신
    s, e, g = map(int, input().split())
    G[s] += [(e, g)]
    G[e] += [(s, g)]

print(dijk(1)[V])
