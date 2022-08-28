def garo(arr):
    global OMOK
    if OMOK:
        return
    for h in range(N):
        dol = 0
        for w in range(N):
            if arr[h][w] == 'o':
                dol += 1
                if dol >= 5:
                    OMOK = True
                    return
            else:
                dol = 0


def sero(arr):
    global OMOK
    if OMOK:
        return
    for w in range(N):
        dol = 0
        for h in range(N):
            if arr[h][w] == 'o':
                dol += 1
                if dol >= 5:
                    OMOK = True
                    return
            else:
                dol = 0


def degak1(arr):
    news = [1, 1]
    global OMOK
    if OMOK:
        return
    for h in range(N-4):
        dol = 0
        for w in range(N-4):
            if arr[h][w] == 'o':
                dol += 1
                x = h
                y = w
                while x < N and y < N:
                    x += news[0]
                    y += news[1]
                    if x == N or y == N:
                        break
                    if arr[x][y] == 'o':
                        dol += 1
                        if dol >= 5:
                            OMOK = True
                            return
                    else:
                        dol = 0
                        break
            else:
                dol = 0

def degak2(arr):
    news = [1, -1]
    global OMOK
    if OMOK:
        return
    for h in range(N - 4):
        dol = 0
        for w in range(N-1, 3, -1):
            if arr[h][w] == 'o':
                dol += 1
                x = h
                y = w
                while x < N and y < N:
                    x += news[0]
                    y += news[1]
                    if x == N or y == N:
                        break
                    if arr[x][y] == 'o':
                        dol += 1
                        if dol >= 5:
                            OMOK = True
                            return
                    else:
                        dol = 0
                        break
            else:
                dol = 0


for tc in range(int(input())):
    N = int(input())
    pan = [list(input()) for _ in range(N)]
    OMOK = False
    garo(pan)
    sero(pan)
    degak1(pan)
    degak2(pan)
    if OMOK:
        print(f'#{tc+1} YES')
    else:
        print(f'#{tc+1} NO')
