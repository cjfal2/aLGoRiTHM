def bfs(G,v,e,V):
    '''
    G : 그래프
    v : 시작점 좌표
    e : 도착점 좌표
    V : 지점 수 
    return : 거리 or 0(불가능)
    * visited에는 노드까지 이동한 거리가 남게됨(못가면0)
    '''
    visited = [0 for _ in range(V+1)] # 방문 리스트 생성 (시작이 0부터 시작할 수 있게, 안 헷갈리게)
    q = []
    q.append(v)
    visited[v] = 1
    while q:         # q가 있으면
        t = q.pop(0) # 첫 번째 원소 반환
        if t==e:     # 도착지면 리턴
            return visited[t]-1 # 1부터 시작되기 때문에 -1을 해줘야함
        for i in G[t]:          # 현재 노드와 연결된 모든 정점에 대해
            if visited[i] == 0: # 방문하지 않은 노드라면 (양방향으로 설정해도 이 부분때문에 다시 돌아가지 않게됨)
                q.append(i)     # 큐에 넣고
                visited[i] = visited[t]+1 # 이동 거리를 늘려줌 
    return 0

for tc in range(int(input())):
    V,E = map(int,input().split())
    G = [[] for _ in range(V+1)]
    for _ in range(E):
        a,b = map(int,input().split())
        G[a] += [b]     
        G[b] += [a]     # 양방향으로 설정을 해줘야함
    # print(G) testcase2 에 대하여
    # [[], [6], [3, 6], [2, 5], [], [3], [1, 2], []]
    # [     1     2       3     4    5      6    7 ]
    s,e = map(int,input().split())
    print(f'#{tc+1} {bfs(G,s,e,V)}')
    # testcase2 에대한 마지막 visited
    # [0, 1, 3, 4, 0, 5, 2, 0]
    # [   1  2  3  4  5  6  7]
    # 1->5