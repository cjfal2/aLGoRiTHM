
def bishop(x, y, cnt, color):
    global where
    if x >= N:
        y += 1
        if x % 2 == 0:
            x = 1
        else:
            x = 0
    if y >= N:
        if cnt > where[color]:
            where[color] = cnt
        return

    if pan[y][x] and not rtol_degak[x+y+1] and not ltor_degak[x-y+N]:
        rtol_degak[x+y+1] = 1
        ltor_degak[x-y+N] = 1
        bishop(x+2, y, cnt+1, color)
        rtol_degak[x+y+1] = 0
        ltor_degak[x-y+N] = 0
    bishop(x+2, y, cnt, color)

rtol_degak = [0 for _ in range(20)]
ltor_degak = [0 for _ in range(20)]
where = [0, 0]
N = int(input())
pan = [list(map(int, input().split())) for _ in range(N)]

# 검은판
bishop(0, 0, 0, 0)
# 흰색판
bishop(1, 0, 0, 1)


print(where[0] + where[1])
