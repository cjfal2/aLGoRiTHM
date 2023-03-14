for tc in range(int(input())):
    N = int(input())
    pan = [[0 for _ in range(N)] for _ in range(N)]
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())

    q = [(sx, sy)]
    pan[sx][sy] = 1
    while q:
        x, y = q.pop(0)
        if x == ex and y == ey:
            print(pan[x][y]-1)
            break

        for dx, dy in (-2,-1), (-2,1), (-1,-2), (-1,2), (1,-2), (1,2), (2,-1), (2,1):
            nx, ny = x + dx, y + dy
            if N > nx >= 0 and N > ny >= 0 and not pan[nx][ny]:
                pan[nx][ny] = pan[x][y] + 1
                q.append((nx, ny))
