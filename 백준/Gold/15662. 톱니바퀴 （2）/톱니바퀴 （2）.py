from collections import deque

N =int(input())
gears = [[-1 for _ in range(8)]] # 패딩 주기
for _ in range(N):
    temp = deque(list(map(int, list(input()))))
    gears.append(temp)
gears.append([-1 for _ in range(8)]) # 패딩 주기

for _ in range(int(input())):
    what, turn = map(int, input().split())
    G = [[what, turn]]

    # 오른쪽 기어들에 영향을 주는지 확인
    right = what
    right_turn = turn
    while right < N:
        if gears[right][2] != gears[right+1][6]:
            G.append([right+1, -right_turn])
            right_turn *= -1
            right += 1
        else:
            break

    # 왼쪽 기어들에 영향을 주는지 확인
    left = what
    left_turn = turn
    while left > 1:
        if gears[left-1][2] != gears[left][6]:
            G.append([left-1, -left_turn])
            left_turn *= -1
            left -= 1
        else:
            break

    for w, t in G:
        gears[w].rotate(t)

answer = 0
for i in range(N):
    if gears[i+1][0]:
        answer += 1
print(answer)
