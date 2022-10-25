def star(n, x, y):
    if n == 1:
        base[y][x] = '*'
    else:
        nn = n//3
        star(nn, x+0*nn, y+0*nn)
        star(nn, x+0*nn, y+1*nn)
        star(nn, x+0*nn, y+2*nn)

        star(nn, x+1*nn, y+0*nn)
        star(nn, x+1*nn, y+2*nn)
        
        star(nn, x+2*nn, y+0*nn)
        star(nn, x+2*nn, y+1*nn)
        star(nn, x+2*nn, y+2*nn)

N = int(input())

base = [[' ' for _ in range(N)] for _ in range(N)]
star(N,0,0)
for a in base:
    print(*a, sep='')