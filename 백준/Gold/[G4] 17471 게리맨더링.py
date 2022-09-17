from itertools import combinations


def bfs(vis, rev):
    # visited 생성 -> N 만큼만 만들어서 인덱스를 잘 조절해야하고,
    # 선거구 1에 대해서만 for문을 돌기 위해서 처음에 -2로 채워줌
    # 방문 안한건 음수 방문 한건 양수
    visited = [-2] * N
    for v1 in vis:  # 선거구 1에 대해서 vistied를 다시 표시? 해줌
        visited[v1-1] = -1

    # -----------선거구 1에 대해서 연결 되어 있는지 확인-----------
    # 위 for문의 마지막 v1이 계속 잔재한다는 것을 과목평가때 알았었음 (그 문제 틀림)
    # 양방향 그래프이기 때문에 아무 구역에서 시작해도 괜찮다고 생각
    # 방문 한건 양수로 처리
    # 선거구를 0부터 받지않고 1부터 받았기 때문에 전체적으로 선거구-1이 많이 들어간 모습
    V = [v1-1]
    visited[v1-1] = -1 * visited[v1-1]
    while V:
        v = V.pop(0)
        if len(G[v]) > 1:
            for i in G[v][1:]:
                if visited[i-1] == -1:
                    V.append(i-1)
                    visited[i-1] = -1 * visited[i-1]

    # -----------선거구 2에 대해서 연결 되어 있는지 확인-----------
    R = [rev[0]-1]
    visited[rev[0]-1] = -1 * visited[rev[0]-1]
    while R:
        r = R.pop(0)
        if len(G[v]) > 1:
            for i in G[r][1:]:
                if visited[i-1] == -2:
                    R.append(i-1)
                    visited[i-1] = -1 * visited[i-1]

    # -----------완성된 visited를 확인해서 인구수 차이를 리턴-----------
    # 방문이 안된 구역이 있으면 끊긴 경우로 -1을 리턴해줌
    if -1 in visited or -2 in visited:
        return -1
    # 선거구에 따른 인구수의 합을 구하고 그 차이의 절대값을 리턴
    else:
        co1 = 0
        co2 = 0
        for idx, geri in enumerate(visited):
            if geri == 1:
                co1 += G[idx][0]
            elif geri == 2:
                co2 += G[idx][0]
        return abs(co1-co2)


N = int(input())
population = list(map(int, input().split()))
G = [[] for _ in range(N)]  # 지역구 그래프 생성

# 생성된 그래프의 지역구에 인구수를 넣어주었음
for po in range(len(population)):
    G[po].append(population[po])

# 연결된 지역구 넣어주기 (연결된 곳이 없다면 인구수만 있겠죠? -> len(G[구역]) == 1)
for n in range(N):
    L = list(map(int, input().split()))
    if len(L) > 1:
        for m in L[1:]:
            G[n] += [m]

# 함수 작업을 위한 사전작업
visit = list(range(1, N+1))     # 원본선거구를 1부터 N까지 만들어줌
ans = []    # 결과를 담을 리스트
for i in range(1, N):
    for v in list(combinations(visit, i)):  # 선거구1
        r = []      # 선거구2

        for vis in visit:   # 원본선거구에서 선거구1에 없는 경우 추가
            if vis not in v:
                r.append(vis)
        # bfs함수 시작
        result = bfs(v, r)
        # -1 이 아닌 경우에만 값을 ans에 저장
        if result > -1:
            ans.append(result)

if not ans:     # 모두 불가능하다면 ans는 빈리스트이므로 따로 처리하여 -1 출력
    print(-1)
else:
    print(min(ans))     # 가장 최소의 인구수 차이를 출력
