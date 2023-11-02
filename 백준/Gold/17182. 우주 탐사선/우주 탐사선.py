import sys
input = sys.stdin.readline
INF = sys.maxsize

N, K = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]

# 플로이드 워셜 알고리즘
for k in range(N):
    for a in range(N):
        for b in range(N):
            G[a][b] = min(G[a][b], G[a][k] + G[k][b])

visited = [0 for _ in range(N)]
visited[K] = 1

answer = INF

# 백트래킹
def dfs(x, y, cnt):
    global answer

    if sum(visited) == N:
        answer = min(answer, cnt)
        return
    
    if answer < cnt:
        return

    for m in range(N):
        if not visited[m]:
            visited[m] = 1
            dfs(y, m, cnt + G[y][m])
            visited[m] = 0


# 모든 점을 시작점으로 해봄
for j in range(N):
    if j == K:
        continue
    
    visited[j] = 1
    dfs(K, j, G[K][j])
    visited[j] = 0

print(answer)