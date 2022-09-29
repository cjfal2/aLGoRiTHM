"""
시작점에 0을 포함하는 무방향 그래프의 다이크스트라
"""
for tc in range(int(input())):
    N, M = map(int, input().split())
    start = 0 # 시작은 이 문제에서 무조건 0
    BIG = 9999999999999

    G = [[] for _ in range(N+1)] # 그라프 생성
    visited = [False for _ in range(N+1)] # 방문 그래프 bool형
    distance = [BIG for _ in range(N+1)] # 거리 저장소

    for _ in range(M): # 그래프 갱신
        s, e, g = map(int, input().split())
        G[s] += [(e, g)]

# 다이크스트라 시작
    distance[start] = 0 # 시작 노드 거리 계산
    visited[start] = True # 시작 노드 방문 처리
    # 인접노드에 대한 최단거리
    for i in G[start]:
        distance[i[0]] = i[1]
    # 시작노드를 제외한 n개의 다른 노드들을 처리
    for _ in range(N):
        # 방문하지 않았고, 시작노드와 최단거리인 노드를 찾음
        MIN = BIG
        now_idx = 0
        for k in range(N+1):
            if not visited[k] and distance[k] < MIN:
                MIN = distance[k]
                now_idx = k
        
        visited[now_idx] = True # 최단거리인 노드를 방문 처리

        for daum in G[now_idx]:
            co = distance[now_idx] + daum[1] # 시작 -> now_idx 거리 + now_idx -> now_idx의 인접노드 거리
            if co < distance[daum[0]]:
                distance[daum[0]] = co

    print(f'#{tc+1} {distance[N]}')
    