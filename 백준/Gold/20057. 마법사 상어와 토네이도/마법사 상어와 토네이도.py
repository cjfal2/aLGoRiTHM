def wind(n, m, direction):
    '''
    n: Y의 x좌표
    m: Y의 y좌표
    direction: D, 방향
    '''
    Y = pan[n][m] # Y의 총량
    Z = 0 # 밖을 넘어간 모래의 양

    two = int(Y * 0.02)
    seven = int(Y * 0.07)
    five = int(Y * 0.05)
    ten =  int(Y * 0.1)
    one = int(Y * 0.01)
    alpha = Y - (two*2) - (seven*2) - five - (ten*2) - (one*2)
    pan[n][m] = 0 # Y를 0으로

    # 4가지 방향일 때 나눔
    if direction == 0: # 좌
        # (n, m+1), (n, m+2) 가 없음
        decas = [(n-2, m), (n-1, m-1), (n-1, m), (n-1, m+1), (n, m-2), (n, m-1), (n+1, m-1), (n+1, m), (n+1, m+1), (n+2, m)]
        score = [two, ten, seven, one, five, alpha, ten, seven, one, two]

    if direction == 1: # 하
        # (n-1, m), (n-2, m) 가 없음
        decas = [(n-1, m-1), (n-1, m+1), (n, m-2), (n, m-1), (n, m+1), (n, m+2), (n+1, m-1), (n+1, m), (n+1, m+1), (n+2, m)]
        score = [one, one, two, seven, seven, two, ten, alpha, ten, five]
    if direction == 2: # 우
        # (n, m-1), (n, m-2) 가 없음
        decas = [(n-2, m), (n-1, m-1), (n-1, m), (n-1, m+1), (n, m+1), (n, m+2), (n+1, m-1), (n+1, m), (n+1, m+1), (n+2, m)]
        score = [two, one, seven, ten, alpha, five, one, seven, ten, two]
    if direction == 3: # 상
        # (n+1, m), (n+2, m) 가 없음
        decas = [(n-2, m), (n-1, m-1), (n-1, m), (n-1, m+1), (n, m-2), (n, m-1), (n, m+1), (n, m+2), (n+1, m-1), (n+1, m+1)]
        score = [five, ten, alpha, ten, two, seven, seven, two, one, one]
    
    for num in range(10):
        a, b = decas[num]
        s = score[num]
        if check(a, b):
            pan[a][b] += s
        else:
            Z += s
    return Z


def check(i, j):
    if N > i >= 0 and N > j >= 0:
        return True
    return False # 범위 안에 있지 않으면 모래 점수로 더해준다.



N = int(input())
pan = [list(map(int, input().split())) for _ in range(N)]

#    좌 하 우 상
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

temp = []
for i in range(1, N+1):
    if i == N:
        temp.append(i-1)
        break
    for _ in range(2):
        temp.append(i)

tona = []
u = 0
for j in temp:
    for _ in range(j):
        tona.append(u)
    u = (u+1) % 4

x, y, d = N//2, N//2, 0

answer = 0
# 토네이도의 점화식
for _ in range(N**2 - 1):
    D = tona[d] # 이동 방향
    # 이동
    nx, ny = x + dx[D], y + dy[D]
    # nx, ny 는 Y 위치임, 여기서 바람일으켜야함
    answer += wind(nx, ny, D)
    # 다음으로 이동
    d += 1
    x, y = nx, ny

print(answer)