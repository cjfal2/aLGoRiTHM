# 입력 처리
def solve():
    K = int(input())
    idx = 1
    results = []

    for k in range(1, K + 1):
        n, m = map(int, input().split())

        # 친구 관계를 저장할 그래프
        graph = {i: set() for i in range(1, n + 1)}

        # 친구 관계
        for _ in range(m):
            a, b = map(int, input().split())

            graph[a].add(b)
            graph[b].add(a)

        # 의심 번호
        s = int(input())

        # s의 친구 목록 및 정렬
        friends = sorted(graph[s])

        print(f"Data Set {k}:")
        if friends:
            print(*friends)
        else:
            print()
        print()


if __name__ == "__main__":
    solve()
