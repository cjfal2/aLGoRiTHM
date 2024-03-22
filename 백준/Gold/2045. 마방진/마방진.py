pan = [list(map(int, input().split())) for _ in range(3)]


def find(pan):
    arr = [pan[0], pan[1], pan[2]]
    arr.append([pan[0][0], pan[1][0], pan[2][0]])
    arr.append([pan[0][1], pan[1][1], pan[2][1]])
    arr.append([pan[0][2], pan[1][2], pan[2][2]])
    arr.append([pan[0][0], pan[1][1], pan[2][2]])
    arr.append([pan[0][2], pan[1][1], pan[2][0]])

    temp = sorted(arr, key=lambda x: x.count(0))[0]
    if 0 in temp:
        return (sum(pan[0]) + sum(pan[1]) + sum(pan[2]))//2
    return sum(temp)


total = int(find(pan))

while 1:
    for i in range(3):
        if pan[i].count(0) == 1:
            pan[i][pan[i].index(0)] = total - sum(pan[i])

    pan2 = list(map(list, zip(*pan)))
    for i in range(3):
        if pan2[i].count(0) == 1:
            pan2[i][pan2[i].index(0)] = total - sum(pan2[i])

    pan = list(map(list, zip(*pan2)))

    for i in range(3):
        if 0 in pan[i]:
            continue
    else:
        break

for i in pan:
    print(*i)
