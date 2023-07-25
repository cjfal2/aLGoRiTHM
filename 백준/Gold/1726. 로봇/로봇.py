N, M = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(N)]
s1, s2, s3 = list(map(int, input().split()))
e1, e2, e3 = tuple(map(int, input().split()))
end = (e1-1, e2-1, e3)
visited = set()
visited.add((s1-1, s2-1, s3))
q = [(s1-1, s2-1, s3, 0)]


def go(i, j, direc):
    if direc == 1:
        j += 1
    elif direc == 2:
        j -= 1
    elif direc == 3:
        i += 1
    else:
        i -= 1
    return i, j


def turn(direction, what):
    if what == "left":
        if direction == 1:
            direction = 4
        elif direction == 2:
            direction = 3
        elif direction == 3:
            direction = 1
        elif direction == 4:
            direction = 2
    else:
        if direction == 1:
            direction = 3
        elif direction == 2:
            direction = 4
        elif direction == 3:
            direction = 2
        elif direction == 4:
            direction = 1
    return direction


#     북4
# 서2    동1
#     남3
# 1, 2, 3, 왼, 오
#
answer = []
while q:
    x, y, d, c = q.pop(0)
    if (x, y, d) == end:
        print(c)
        quit()

    for command in ["1", "2", "3", "left", "right"]:
        nx, ny, nd = x, y, d
        flag = False
        if command == "1":
            nx, ny = go(nx, ny, d)

            if not (N > nx >= 0) or not (M > ny >= 0) or pan[nx][ny]:
                flag = True
            if flag:
                continue
        elif command == "2":
            for _ in range(2):
                nx, ny = go(nx, ny, d)

                if not (N > nx >= 0) or not (M > ny >= 0) or pan[nx][ny]:
                    flag = True
                    break
            if flag:
                continue
        elif command == "3":
            for _ in range(3):
                nx, ny = go(nx, ny, d)

                if not (N > nx >= 0) or not (M > ny >= 0) or pan[nx][ny]:
                    flag = True
                    break
            if flag:
                continue
        elif command == "left":
            nd = turn(d, "left")
        elif command == "right":
            nd = turn(d, "right")

        if N > nx >= 0 and M > ny >= 0 and (nx, ny, nd) not in visited and not pan[nx][ny]:
            visited.add((nx, ny, nd))
            q.append((nx, ny, nd, c + 1))

