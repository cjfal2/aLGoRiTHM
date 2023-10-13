'''
1. 토네이도 구슬 땅기기 구현
2. 폭파 구현
3. 토네이도 구슬 생기기 구현 (연속하는거에서 개수먼저, 무슨 숫자인지 다음)
'''


def blizard(d, s):
    '''
    블리자드 함수
    d방향 s만큼 구슬을 파괴한다.
    '''
    x, y = N//2, N//2  # 시작 상어 위치
    for _ in range(s):
        x, y = x + dx[d], y + dy[d]
        pan[x][y] = 0


def make_tornado(n):
    '''
    토네이도 만들기 함수
    '''
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

    wind = []
    u = 0
    for j in temp:
        for _ in range(j):
            wind.append(u)
        u = (u+1) % 4

    decas = []
    x, y, d = N//2, N//2, 0

    # 토네이도의 점화식
    for _ in range(N**2 - 1):
        D = wind[d]  # 이동 방향
        # 이동
        nx, ny = x + dx[D], y + dy[D]
        decas.append((nx, ny))
        # 다음으로 이동
        d += 1
        x, y = nx, ny
    return decas


def bomb():
    '''
    폭발시키는 함수 4개 이상 토네이도로 붙어있으면 폭발한다.
    토네이도 좌표를 순회하면서 연속 4개이상이면 바로 부신다.

    여기서 4개이상 겹치는게 하나도 없으면 구슬 생성으로 이동
    아니면 중력작용
    '''
    box = {
        1: [],
        2: [],
        3: []
    }  # 폭발시킬 좌표들, 이거로 점수 계산
    now_beads = pan[winds[0][0]][winds[0][1]]  # 첫번째 구슬의 숫자
    # 2번째구슬부터 시작하여 겹치는지 판단한 후 4개이상인데 다음이 없거나 숫자가 바뀌면 box에 추가
    number = 1
    temp = [tuple(winds[0])]
    score = 0  # 폭발 점수

    for x, y in winds[1:]:
        if pan[x][y] == 0:
            if number >= 4:
                box[now_beads].extend(temp)
                score += (now_beads * number)
            break
        # 같은 구슬이라면
        if now_beads == pan[x][y]:
            number += 1
            temp.append((x, y))
            # 마지막에 도달했는데 같은 구슬일 경우
            if x == 0 and y == 0 and number >= 4:
                box[now_beads].extend(temp)
                score += (now_beads * number)

        # 다른 구슬이라면
        else:
            if number >= 4:
                # 결과 저장
                box[now_beads].extend(temp)
                score += (now_beads * number)
            # 새로 설정
            temp = [(x, y)]
            now_beads = pan[x][y]
            number = 1

    for val in box.values():
        for x, y in val:
            pan[x][y] = 0
    return score


def gravity():
    '''
    (N//2, N//2 - 1) 에서부터 시작하여 중력을 토네이도 모양으로 작용한다.
    0 인 경우 상어 위치가 아니라면 중력을 작용
    '''
    idx = 0
    while idx < N*N - 1:
        x, y = winds[idx]
        if pan[x][y] == 0: # 0인 경우
            bx, by = winds[idx]  # 맨 아래 구슬의 좌표
            bidx = idx # 맨 아래 구슬의 위치
            idx += 1
            while idx < N*N - 1:
                nx, ny = winds[idx]
                # 여전히 0인 경우
                if pan[nx][ny] == 0:
                    idx += 1
                else: # 숫자일 경우
                    pan[bx][by] = pan[nx][ny] # 맨아래 구슬로 이동
                    pan[nx][ny] = 0 # 그 위치 0으로
                    idx = bidx
                    break
        else:
            idx += 1
    # 손좀 봐야함 중력 작용: 끝에서 에러날수도있음
                    



def make_beads():
    '''
    토네이도로 돌면서 연속하는거 확인
    '''
    real = []
    now_beads = pan[winds[0][0]][winds[0][1]]
    number = 1
    for x, y in winds[1:]:
        # 같은 구슬이라면
        if pan[x][y] == now_beads:
            number += 1
            

        # 다른 구슬이라면
        else:
            real.append(number)
            real.append(now_beads)
            # 새로 설정
            now_beads = pan[x][y]
            number = 1
    new_pan = [[0 for _ in range(N)] for _ in range(N)]
    i = 0
    for x, y in winds:
        if i == len(real):
            break
        new_pan[x][y] = real[i]
        i += 1
    return new_pan




N, M = map(int, input().split())  # N: 격자 크기(홀수), M: 마법 시전 수
pan = [list(map(int, input().split())) for _ in range(N)]  # 판
info_blizard = []
    
# 방향, 상0 하1 좌2 우3
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


winds = make_tornado(N)  # 토네이도 순서로 좌표가 들어가 있다.
answer = 0
# 주문 시젼 수 만큼
for _ in range(M):
    blizard_d, blizard_s = map(int, input().split())  # [방향d, 거리s]
    blizard_d -= 1
    blizard(blizard_d, blizard_s)
    gravity()

    # 파괴 중력 반복
    while 1:
        A = bomb()
        gravity()
        answer += A
        if A == 0:
            pan = make_beads()
            break
print(answer)
