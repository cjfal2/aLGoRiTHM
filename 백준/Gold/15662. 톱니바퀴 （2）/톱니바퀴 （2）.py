'''
톱니가 맞물린 극이 다를 때만 회전에 영향을 준다.
톱니 8개 중 맞닿아 있는 (0부터 시작) 부분은 왼쪽 2과 오른쪽 6 부분이다. 

시계1 / 반시계-1 로 한 칸의 톱니만 회전 가능
톱니바퀴는 1, 2, 3, 4     4개 가 있고  양 옆 바퀴에만 영향이 간다.
3번이 움직일 때 2, 4 번이 움직일 수 있고, 1번에는 영향이 가지 않는데, 이 때 2번이 1번에 영향을 줄 수 있으면 1번도 움직인다.
톱니바퀴마다 점수가 다르다.

N극은 0 S극은 1이다.
--------------풀이전략--------------------------
톱니바퀴이므로 deque를 이용한다.

'''


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
