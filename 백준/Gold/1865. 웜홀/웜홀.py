def solve(n, arr):
    visited = [100000 for _ in range(n+1)]
    visited[1] = 0

    for _ in range(n):
        for u, v, c in arr:
            if visited[u] + c < visited[v]:
                visited[v] = visited[u] + c

    for u, v, c in arr:
        if visited[u] + c < visited[v]:
            return True

    return False


for _ in range(int(input())):
    n, m, w = map(int, input().split())
    edges = []

    for _ in range(m):
        start, end, cost = map(int, input().split())
        edges.append((start, end, cost))
        edges.append((end, start, cost))

    for _ in range(w):
        start, end, cost = map(int, input().split())
        edges.append((start, end, -cost))

    print("YES" if solve(n, edges) else "NO")