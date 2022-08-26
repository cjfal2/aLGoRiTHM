def center(pan):
    mid = N//2
    pan[mid-1][mid] = pan[mid][mid-1] = 1
    pan[mid-1][mid-1] = pan[mid][mid] = 2

def count_color(pan):
    co_B = 0
    co_W = 0
    for x in pan:
        co_B+=x.count(1)
        co_W+=x.count(2)
    return co_B,co_W

def oselo(pan,Y,H,C):
    if C == 1:
        c = 1
        cr = 2
    else:
        c = 2
        cr = 1
    H-=1
    Y-=1
    pan[H][Y]=c
    for nx,ny in [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]:
        h = H+nx
        y = Y+ny

        check = False
        L = []
        while 0<=h<N and 0<=y<N:
            if pan[h][y] == c:
                check = True
                break
            if pan[h][y] == 0:
                break
            L.append([h,y])
            h += nx
            y += ny
        if check:
            for i,j in L:
                pan[i][j]=c

for tc in range(int(input())):
    N, M = map(int,input().split())
    pan = [[0 for _ in range(N)] for _ in range(N)]
    center(pan)
    for _ in range(M):
        Y, H, C = map(int,input().split())
        oselo(pan,Y,H,C)
    a,b = count_color(pan)
    print(f'#{tc+1} {a} {b}')