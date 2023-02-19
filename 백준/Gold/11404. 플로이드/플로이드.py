import sys
input = sys.stdin.readline
INF = sys.maxsize

# 노드의 개수(N)과 간선의 개수(M) 입력
N = int(input().strip())
M = int(input().strip())

# 2차원 거리 정보 리스트 만듦(무한대를 기본값으로 줌)
G = [[INF for _ in range(N + 1)] for _ in range(N + 1)]

# 자기 자신 -> 자기 자신 => 0으로
for a in range(1, N + 1):
    for b in range(1, N + 1):
        if a == b:
            G[a][b] = 0

# 거리를 입력받고, 원래 있던 것과 비교하여 원래있던 것 보다 작으면 넣어줌
for _ in range(M):
    # a에서 b로 가는 비용이 c
    a, b, c = map(int, input().strip().split())
    if G[a][b] > c:
        G[a][b] = c

# 플로이드 워셜 알고리즘
for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            G[a][b] = min(G[a][b], G[a][k] + G[k][b])

# 아웃풋
for a in range(1, N + 1):
    for b in range(1, N + 1):
        if G[a][b] != INF:
            print(G[a][b], end=" ")
        else: 
            print(0, end=" ")
    print()