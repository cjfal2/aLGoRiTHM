import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline

# 입력 받기
N, S, D = map(int, input().split())

# 트리 저장 (인접 리스트)
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 깊이 정보 저장
depth = [0] * (N + 1)
ans = 0

# DFS 수행
def dfs(node, before):
    global ans
    for next_node in graph[node]:
        if next_node != before:
            depth[node] = max(depth[node], dfs(next_node, node) + 1)
    
    # 노드의 깊이가 D 이상이고, 루트(S)가 아니라면 왕복 필요
    if depth[node] >= D and node != S:
        ans += 1

    return depth[node]

# DFS 탐색 시작
dfs(S, -1)

# 왕복 거리 계산하여 출력
print(ans * 2)
