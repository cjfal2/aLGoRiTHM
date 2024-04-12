"""
1. 상어가 모든 물고기에게 복제 마법을 시전한다.
   복제 마법은 시간이 조금 걸리기 때문에, 아래 5번에서 물고기가 복제되어 칸에 나타난다.

2. 모든 물고기가 한 칸 이동한다. 상어가 있는 칸, 물고기의 냄새가 있는 칸, 격자의 범위를 벗어나는 칸으로는 이동할 수 없다.
각 물고기는 자신이 가지고 있는 이동 방향이 이동할 수 있는 칸을 향할 때까지 "방향을 45도 반시계 회전"시킨다.
만약, 이동할 수 있는 칸이 없으면 "이동을 하지 않는다". 그 외의 경우에는 그 칸으로 이동을 한다. 물고기의 냄새는 아래 3에서 설명한다.

3. 상어가 연속해서 3칸 이동한다. 상어는 현재 칸에서 "상하좌우로 인접한 칸"으로 이동할 수 있다.
연속해서 이동하는 칸 중에 격자의 범위를 벗어나는 칸이 있으면, 그 방법은 불가능한 이동 방법이다.
연속해서 이동하는 중에 상어가 물고기가 있는 같은 칸으로 이동하게 된다면, 그 칸에 있는 "모든 물고기"는 격자에서 제외되며,
"제외되는 모든 물고기"는 "물고기 냄새"를 남긴다. 가능한 이동 방법 중에서 "제외되는 물고기의 수가 가장 많은 방법"으로 이동하며,
그러한 방법이 여러가지인 경우 "사전 순으로 가장 앞서는 방법"을 이용한다. {상은 1, 좌는 2, 하는 3, 우는 4}

4. 두 번 전 연습에서 생긴 물고기의 냄새가 격자에서 사라진다.

5. 1에서 사용한 복제 마법이 완료된다. 모든 복제된 물고기는 1에서의 위치와 방향을 그대로 갖게 된다.
격자에 있는 물고기의 위치, 방향 정보와 상어의 위치, 그리고 연습 횟수 S가 주어진다. S번 연습을 모두 마쳤을때, 격자에 있는 물고기의 수를 구해보자.
"""
from itertools import permutations


def move_shark(si, sj):
    global shark_place, new_pan

    max_count = -1
    max_permu = []
    for permu in permutations(shark_permu, 3):
        ni, nj = si, sj
        temp_count = 0
        visited_fished = set()
        for sd in permu:
            dx, dy = shark_directions[sd]
            ni, nj = ni + dx, nj + dy
            if 4 > ni >= 0 and 4 > nj >= 0:
                if (ni, nj) not in visited_fished:
                    temp_count += len(new_pan[ni][nj])
                    visited_fished.add((ni, nj))
            else:
                break
        else:
            if max_count < temp_count:
                max_count = temp_count
                max_permu = permu
    # print(max_permu)
    # print(max_count)
    for sd in max_permu:
        si, sj = si + shark_directions[sd][0], sj + shark_directions[sd][1]
        if len(new_pan[si][sj]) > 0:
            new_pan[si][sj] = []
            smells_turn[(si, sj)] = 0

    shark_place = (si, sj)
    return


fish_directions = [(0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
#                              ←1      ↖2        ↑3       ↗4      →5      ↘6      ↓7      ↙8

shark_permu = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]

shark_directions = {
    1: (-1, 0),
    2: (0, -1),
    3: (1, 0),
    4: (0, 1)  # 상 좌 하 우
}

pan = [[[] for _ in range(4)] for _ in range(4)]
M, S = map(int, input().split())  # 물고기의 수 M, 상어가 마법을 연습한 횟수 S
for _ in range(M):
    i, j, d = map(int, input().split())
    pan[i - 1][j - 1].append(d)

shark_place = tuple(map(lambda x: int(x) - 1, input().split()))
smells_turn = dict()

# for p in pan:
#     print(*p)
# print()

for s in range(S):
#     print(f"턴: {s}, 지금 상어:{shark_place}, 냄새: {smells_turn}")
    new_pan = [[[] for _ in range(4)] for _ in range(4)]
    for n in range(4):
        for m in range(4):
            for d in pan[n][m]:
                dd = d
                for _ in range(8):
                    nx, ny = n + fish_directions[dd][0], m + fish_directions[dd][1]
                    if 4 > nx >= 0 and 4 > ny >= 0 and (nx, ny) != shark_place and (nx, ny) not in smells_turn:
                        new_pan[nx][ny].append(dd)
                        break
                    else:
                        dd -= 1
                        if dd == 0:
                            dd = 8
                else:
                    new_pan[n][m].append(d)
#     for l in new_pan:
#         print(*l)
#     print("뉴판")
    move_shark(*shark_place)
#     for l in new_pan:
#         print(*l)
    # print("제거뉴판")
    for n in range(4):
        for m in range(4):
            pan[n][m].extend(new_pan[n][m])

    remove_smell = set()
    for k, v in smells_turn.items():
        smells_turn[k] += 1
        if v == 2:
            remove_smell.add(k)
    # print(remove_smell, "제거 스멜")
    for k in remove_smell:
        # print(k)
        smells_turn.pop(k)

    # for p in pan:
    #     print(*p)
    # print(smells_turn)
    # print(f"-=---상어위치 {shark_place}-----복제---------")
    # print()

answer = 0
for n in range(4):
    for m in range(4):
        answer += len(pan[n][m])
print(answer)
