def back(idx):
    global answer

    if idx == N:
        temp = 0
        for z in range(N):
            if pan[z][0] <= 0:
                temp += 1
        answer = max(answer, temp)
        return

    if pan[idx][0] <= 0:
        back(idx+1)
        return

    flag = True
    h, w = pan[idx]
    for i in range(N):
        if i == idx:
            continue

        a, b = pan[i]
        if a <= 0:
            continue

        flag = False
        pan[idx][0] -= b
        pan[i][0] -= w
        back(idx+1)
        pan[i][0] += w
        pan[idx][0] += b

    if flag:
        back(N)


N = int(input())
pan = [list(map(int, input().split())) for _ in range(N)]
answer = 0
back(0)
print(answer)
