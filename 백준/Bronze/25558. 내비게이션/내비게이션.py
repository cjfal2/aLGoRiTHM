N = int(input())
sx, sy, ex, ey = map(int, input().split())
MIN = float("INF")
answer = 0

for navi in range(1, N+1):
    M = int(input())
    nx, ny = sx, sy
    move = 0
    for _ in range(M):
        a, b = map(int, input().split())
        move += abs(nx - a)
        move += abs(ny - b)
        nx, ny = a, b
    move += abs(ex - nx)
    move += abs(ey - ny)
    if MIN > move:
        MIN = move
        answer = navi
print(answer)