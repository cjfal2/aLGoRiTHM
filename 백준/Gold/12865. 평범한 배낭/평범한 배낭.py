import sys
input = sys.stdin.readline

def goonjang():
    for i in range(N+1):
        G[i][0] = 0
    for w in range(K+1):
        G[0][w] = 0

    for i in range(1, N+1):
        for w in range(1, K+1):
            if weight[i] > w:
                G[i][w] = G[i-1][w]
            else:
                G[i][w] = max(G[i-1][w-weight[i]] + value[i], G[i-1][w])
    print(G[N][K])


N, K = map(int, input().strip().split()) # 물건의 수, 가능한 무게
weight = [0] # 물건의 무게들
value = [0] # 물건의 무게들
for _ in range(N):
    W, V = map(int, input().strip().split()) # 물건의 무게, 물건의 가치
    weight.append(W)
    value.append(V)

G = [[-1 for _ in range(K+1)] for _ in range(N+1)] # DP로 쓸 2차원 배열을 선언한다.

goonjang()