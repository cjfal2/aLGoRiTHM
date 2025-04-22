import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

class DSU:
    def __init__(self, n):
        self.p = [-1] * (n + 1)
    def find(self, x):
        if self.p[x] < 0:
            return x
        self.p[x] = self.find(self.p[x])
        return self.p[x]
    def unite(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return False
        if self.p[a] > self.p[b]:
            a, b = b, a
        self.p[a] += self.p[b]
        self.p[b] = a
        return True

def main():
    N, M, K = map(int, input().split())
    edges = []
    # 가중치는 입력 순서대로 1..M
    for w in range(1, M + 1):
        u, v = map(int, input().split())
        edges.append((w, u, v, w))  # (weight, u, v, id)
    edges.sort(key=lambda e: e[0])

    removed = [False] * (M + 1)
    ans = []
    fail = False

    for _ in range(K):
        if fail:
            ans.append(0)
            continue

        dsu = DSU(N)
        cost = 0
        mst_edges = []

        # Kruskal: MST 구성
        for w, u, v, eid in edges:
            if removed[eid]:
                continue
            if dsu.unite(u, v):
                cost += w
                mst_edges.append((w, eid))
                if len(mst_edges) == N - 1:
                    break

        # MST 불가능 시 이후 턴은 모두 0
        if len(mst_edges) < N - 1:
            ans.append(0)
            fail = True
        else:
            ans.append(cost)
            # MST에서 가장 작은 가중치 간선 제거
            smallest_id = mst_edges[0][1]
            removed[smallest_id] = True

    print(' '.join(map(str, ans)))

if __name__ == "__main__":
    main()
