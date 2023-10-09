k = int(input())
command = input().split()[::-1]  # 뒤부터 시작할 것임

N = 2 ** k
paper = [[0 for _ in range(N)] for _ in range(N)]  # 전체 펼쳤을 때 종이 크기
paper[0][0] = int(input())  # 첫번째 뚫은 위치를 표시

LR = {
    0: 1,
    1: 0,
    2: 3,
    3: 2,
}
UD = {
    0: 2,
    1: 3,
    2: 0,
    3: 1,
}


sero, garo = 1, 1  # 다 접었을 때 세로와 가로 크기, 펼때마다 펴진쪽을 2 늘려줄 것임
for what in command:
    # L, U는 판의 시작점이 달라지지 않음, 새로운거만 표시하면 됨
    if what == 'L':
        for s in range(sero):
            for g in range(garo):
                paper[s][2 * garo - 1 - g] = LR[paper[s][g]]
        garo *= 2

    elif what == 'U':
        for s in range(sero):
            for g in range(garo):
                paper[2 * sero - 1 - s][g] = UD[paper[s][g]]
        sero *= 2

    # R, D는 판의 시작점이 달라짐
    elif what == 'R':
        for s in range(sero):
            for g in range(garo):
                paper[s][g + garo] = paper[s][g]
        for s in range(sero):
            for g in range(garo):
                paper[s][g] = LR[paper[s][2 * garo - 1 - g]]
        garo *= 2

    elif what == 'D':
        for s in range(sero):
            for g in range(garo):
                paper[s + sero][g] = paper[s][g]
        for s in range(sero):
            for g in range(garo):
                paper[s][g] = UD[paper[2 * sero - 1 - s][g]]
        sero *= 2

    # for v in paper:
    #     print(*v)
    # print("==================")

for v in paper:
    print(*v)
