def solve():
    for tc in range(1, int(input()) + 1):
        n, m = map(int, input().split())
        info = {i: set() for i in range(1, n + 1)}
        for _ in range(m):
            a, b = map(int, input().split())
            info[a].add(b)
            info[b].add(a)

        friends = sorted(info[int(input())])

        print(f"Data Set {tc}:")
        print(*friends) if friends else print()
        print()


if __name__ == "__main__":
    solve()
