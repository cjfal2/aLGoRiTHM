def fill(x1, y1, k):
    for x2 in range(k):
        for y2 in range(k):
            if not pan[x1+x2][y1+y2]:
                return False
    return True


def vis(a1, b1, kkan, boool):
    global pan, total
    for a2 in range(kkan):
        for b2 in range(kkan):
            pan[a1+a2][b1+b2] = boool
            if boool == 0:
                total -= 1
            else:
                total += 1


def origami(x, y, su):
    global co, total

    if co < su:
        return

    if total == 0 and co > su:
        co = su
        return

    if y >= 10:
        return

    if x >= 10:
        origami(0, y+1, su)
        return

    if pan[x][y] == 1:
        for k in range(5, 0, -1):
            if base[k] and x - 1 + k < 10 and y - 1 + k < 10 and fill(x, y, k):
                vis(x, y, k, 0)
                base[k] -= 1
                origami(x + k, y, su + 1)
                base[k] += 1
                vis(x, y, k, 1)

    else:
        origami(x + 1, y, su)


base = [5 for _ in range(6)] # 색종이가 5개씩 있으니까~   (0은 무시)
pan = []
total = 0
for vv in range(10): # 뽀문 바로 돌면서 total이랑 pan을 채워줌
    a = list(map(int, input().split()))
    pan.append(a)
    total += a.count(1)

co = 9999999999 # 겁나 큰애 넣어줌

origami(0, 0, 0) # dfs 시작

if co != 9999999999: # co가 변했다면
    print(co)
else: # 안변했다면
    print(-1)