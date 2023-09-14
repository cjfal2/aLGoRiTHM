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


gears = [[]]  # 패딩 주기
for _ in range(4):
    temp = deque(list(map(int, list(input()))))
    gears.append(temp)

for _ in range(int(input())):
    what, turn = map(int, input().split())
    G = [[what, turn]]

    if what == 1:
        # 오른쪽 기어들에 영향을 주는지 확인
        if gears[1][2] != gears[2][6]:
            G.append([2, -turn])
            if gears[2][2] != gears[3][6]:
                G.append([3, turn])
                if gears[3][2] != gears[4][6]:
                    G.append([4, -turn])
    elif what == 4:
        # 왼쪽 기어들에 영향을 주는지 확인
        if gears[3][2] != gears[4][6]:
            G.append([3, -turn])
            if gears[2][2] != gears[3][6]:
                G.append([2, turn])
                if gears[1][2] != gears[2][6]:
                    G.append([1, -turn])
    elif what == 2:
        # 1번 기어에 영향을 주는지 확인
        if gears[1][2] != gears[2][6]:
            G.append([1, -turn])
        # 3번 기어에 영향을 주는지 확인
        if gears[2][2] != gears[3][6]:
            G.append([3, -turn])
            # 4번 기어에 영향을 주는지 확인
            if gears[3][2] != gears[4][6]:
                G.append([4, turn])
    elif what == 3:
        # 4번 기어에 영향을 주는지 확인
        if gears[3][2] != gears[4][6]:
            G.append([4, -turn])
        # 2번 기어에 영향을 주는지 확인
        if gears[2][2] != gears[3][6]:
            G.append([2, -turn])
            # 1번 기어에 영향을 주는지 확인
            if gears[1][2] != gears[2][6]:
                G.append([1, turn])

    for w, t in G:
        gears[w].rotate(t)

answer = 0
for i in range(4):
    if gears[i+1][0]:
        answer += (2**i)
print(answer)
