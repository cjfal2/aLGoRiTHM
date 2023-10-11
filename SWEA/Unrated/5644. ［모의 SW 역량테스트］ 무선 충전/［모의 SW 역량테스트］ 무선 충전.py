'''
# 충전소 정보도 표시해야함
# 충전소 마름모 꼴로 나타내야함 
- 충전소 겹치는 부분 처리해야함

# 지나 가면서 동시에 최대값 갱신??
-  0     1   2  3   4
 멈춤   상 우 하 좌 
'''


def charge(A, B):
    res = 0
    
    BC_A = BC.get(A)
    BC_B = BC.get(B)
    if BC_A and BC_B:
        for aa in BC_A:
            for bb in BC_B:
                if aa == bb:
                    res = max(res, info.get(aa))
                else:
                    res = max(res, info.get(aa) + info.get(bb))
    elif BC_A:
        for aa in BC_A:
            res = max(res, info.get(aa))
    elif BC_B:
        for bb in BC_B:
            res = max(res, info.get(bb))
    
    return res
    

for tc in range(1, int(input())+1):
    M, T = map(int, input().split())  # M: 총 이동 시간, T: BC의 개수
    A_move = list(map(int, input().split()))
    B_move = list(map(int, input().split()))

    BC = dict() # 충전소 정보
    info = dict() # 충전량 정보

    for z in range(1, T+1):# z: 충전소 번호
        y, x, c, p = map(int, input().split()) # y: x좌표 x: y좌표 c: 충전범위, p: 충전량
        y -= 1
        x -= 1
        info[z] = p
        for i in range(x-c, x+c+1):
            for j in range(y-c, y+c+1):
                if 10 > i >= 0 and 10 > j >= 0 and c >= (abs(i-x) + abs(j-y)):
                    if not BC.get((i, j)):
                        BC[(i, j)] = [z]
                    else:
                        BC[(i, j)].append(z)
                    
    # print(BC)
    # print(info)

    # 멈춤, 상, 우, 하, 좌
    dx = [0, -1, 0, 1, 0]
    dy = [0, 0, 1, 0, -1]

    answer = 0
    a = (0, 0) # a 위치
    b = (9, 9) # b 위치

    answer += charge(a, b)  # 처음 자리 충전확인
    for m in range(M):
        # 이동 후 충전확인
        a = (a[0] + dx[A_move[m]], a[1] + dy[A_move[m]])
        b = (b[0] + dx[B_move[m]], b[1] + dy[B_move[m]])
        answer += charge(a, b)
    print(f'#{tc} {answer}')
