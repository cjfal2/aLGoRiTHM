def solve():
    N, M, K = map(int, input().split())
    wall = set()
    for _ in range(K):
        a, b = map(int, input().split())
        wall.add((a, b))
    da = ((-1, 0), (-1, 1), (0, -1), (0, 1), (1, 0), (1, 1))
    db = ((-1, -1), (-1, 0), (0, -1), (0, 1), (1, -1), (1, 0))
    visited = set()
    visited.add((0, 0))
    q = [(0, 0, 0)]
    while q:
        x, y, cnt = q.pop(0)
        if (x, y) == (N-1, M-1):
            return cnt
        for dx, dy in da if x % 2 else db:
            nx, ny = x + dx, y + dy
            if N > nx >= 0 and M > ny >= 0 and (nx, ny) not in wall and (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append((nx, ny, cnt+1))
    return -1
print(solve())