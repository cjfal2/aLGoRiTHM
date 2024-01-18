pan = []
target = 0
for _ in range(3):
    temp = list(map(int, input().split()))
    target += sum(temp)
    pan.append(temp)

# 합을 못구했을 경우의 타겟값은 전체 합의 절반으로 해둔다.
target //= 2

# 행에 타겟 합이 있는지 확인
for p in pan:
    if 0 not in p:
        target = sum(p)

# 열에 타겟 합이 있는지 확인
for p in list(zip(*pan)):
    if 0 not in p:
        target = sum(p)

# 좌상 우하 대각에 합이 있는지 확인
if pan[0][0] and pan[1][1] and pan[2][2]:
    target = pan[0][0] + pan[1][1] + pan[2][2]

# 우상 좌하 대각에 합이 있는지 확인
if pan[0][2] and pan[1][1] and pan[2][0]:
    target = pan[0][2] + pan[1][1] + pan[2][0]

# 행에 있는 혼자인 0 채우기
for i in range(3):
    if pan[i].count(0) == 1:
        where_zero = pan[i].index(0)
        pan[i][where_zero] = target - sum(pan[i])

# 열에 있는 혼자인 0 채우기
pan = list(map(list, list(zip(*pan)))) # zip은 튜플로 들어감
for i in range(3):
    if pan[i].count(0) == 1:
        where_zero = pan[i].index(0)
        pan[i][where_zero] = target - sum(pan[i])

# 되돌리기
pan = list(zip(*pan))

# 출력
for p in pan:
    print(*p)
