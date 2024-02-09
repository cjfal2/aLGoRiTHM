pan = [[0 for _ in range(8)] for _ in range(8)]
a, b = map(lambda x: int(x) - 1, input().split())
pan[a][b] = 1
end = tuple(map(lambda x: int(x) - 1, input().split()))

q = [(a, b)]
while q:
    x, y = q.pop(0)
    if (x, y) == end:
        print(pan[x][y]-1)
        break
    for dx, dy in (2, 1), (-2, 1), (2, -1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2):
        nx, ny = x + dx, y + dy
        if 8 > nx >= 0 and 8 > ny >= 0 and not pan[nx][ny]:
            pan[nx][ny] = pan[x][y] + 1
            q.append((nx, ny))
            