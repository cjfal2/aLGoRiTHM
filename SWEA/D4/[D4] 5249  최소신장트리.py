for tc in range(int(input())):
    V, E = map(int, input().split())

    INF = 10000
    # 인접행렬
    G = [[INF]*(V+1) for _ in range(V+1)]

    for i in range(V+1):
        G[i][i] = 0

    for _ in range(E):
        u, v, w = map(int, input().split())
        G[u][v] = w
        G[v][u] = w 

    key = [INF]*(V+1)
    key[0] = 0
    MST = [0] * (V+1)
    pi = [0] * (V+1)

    for _ in range(V+1):
        u = 0
        MIN = INF
        for i in range(V+1):
            if MST[i]==0:
                if key[i] < MIN:
                    u = i
                    MIN = key[i]
        MST[u] = 1
        for v in range(V+1):
            if MST[v] == 0 and u!=v and G[u][v]< INF:
                if key[v] > G[u][v]:
                    key[v] = G[u][v]
                    pi[v] = u 
    print(f'#{tc+1} {sum(key)}')