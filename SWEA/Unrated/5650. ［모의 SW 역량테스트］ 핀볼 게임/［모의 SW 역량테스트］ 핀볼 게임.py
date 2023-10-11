walls = {
    1: {0: 2, 1: 3, 2: 1, 3: 0},
    2: {0: 1, 1: 3, 2: 0, 3: 2},
    3: {0: 3, 1: 2, 2: 0, 3: 1},
    4: {0: 2, 1: 0, 2: 3, 3: 1},
    5: {0: 2, 1: 3, 2: 0, 3: 1},
}

#     북  동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for tc in range(1, int(input())+1):
    N = int(input())
    wormhole = dict()
    pan = []
    start = []

    for i in range(N):
        temp = list(map(int, input().split()))
        for j in range(N):
            w = temp[j]
            if w == 0:
                start.append((i+1, j+1))
            elif w in [6, 7, 8, 9, 10]:
                if w in wormhole:
                    wormhole[w].append((i+1, j+1))
                else:
                    wormhole[w] = [(i+1, j+1)]
        pan.append([5] + temp + [5])
    pan = [[5 for _ in range(N+2)]] + pan + [[5 for _ in range(N+2)]]
    answer = 0
    # 시작 지점들
    for x, y in start:
        # 시작 지점 기억
        memo = (x, y)
        # 4가지 방향
        for d in [0, 1, 2, 3]:
            x, y = memo
            score = 0  # 부딪힌 횟수
            # 시작
            # print("=============") 
            # print(x, y, d, "시작지점")
            while 1:
                nx, ny, nd = x + dx[d], y + dy[d], d
                # 안 쪽 상황
                if N+1 > nx >= 1 and N+1 > ny >= 1:
                    X = pan[nx][ny] # 핀볼
                    # 블랙홀 맞은 경우 또는 시작점일 경우
                    if X == -1 or (nx, ny) == memo:
                        answer = max(answer, score)
                        # print("끝1")
                        break

                    # 벽에 부딪힌 경우
                    elif X in [1, 2, 3, 4, 5]:
                        nd = walls[X][d]
                        score += 1

                    # 웜홀에 부딪힌 경우
                    elif X in [6, 7, 8, 9, 10]:
                        for a, b in wormhole[X]:
                            if a != nx or b != ny:
                                nx, ny = a, b
                                break

                    # 빈 공간이거나 진행 했을경우
                    # print(nx, ny, nd)

                else:  # 끝쪽 벽에 부딪힌 경우
                    nd = walls[5][d]
                    score += 1
                    # print(nx, ny, d, "끝쪽")
                x, y, d = nx, ny, nd
    print(f"#{tc} {answer}")    
            
