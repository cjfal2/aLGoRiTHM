import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # 경로 압축 최적화
    return parent[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            rank[root_x] += 1  # 랭크 업데이트

V, E = map(int, input().split())
edges = []

for _ in range(E):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

edges.sort()  # 간선을 가중치 기준으로 정렬

parent = [i for i in range(V + 1)]
rank = [0] * (V + 1)

mst_weight = 0
edge_count = 0

for w, u, v in edges:
    if find(u) != find(v):  # 사이클이 생기지 않으면 선택
        union(u, v)
        mst_weight += w
        edge_count += 1
        if edge_count == V - 1:  # MST 완성
            break

print(mst_weight)
