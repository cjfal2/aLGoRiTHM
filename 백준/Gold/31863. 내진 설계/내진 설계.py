N, M = map(int, input().split())
pan = []
buildings = dict()
earthquake = []
walls = set()
for n in range(N):
    temp = list(input()) 
    pan.append(temp)
    for m in range(M):
        if temp[m] == "*":
            buildings[(n, m)] = 1
        elif temp[m] == "@":
            earthquake.append([n, m])
        elif temp[m] == "|":
            walls.add((n, m))
        elif temp[m] == "#":
            buildings[(n, m)] = 2
total = len(buildings)
total_answer = len(buildings)

dix = [(1, 0), (-1, 0), (0, 1), (0, -1)]
# 지진 시작
x, y = earthquake.pop(0)
pan[x][y] = "|"
walls.add((x, y))
for dx, dy in dix:
    nx, ny = x, y
    for _ in range(2):
        nx += dx
        ny += dy
        if N > nx >= 0 and M > ny >= 0 and (nx, ny) not in walls:
            what = pan[nx][ny]
            if what in "*#":
                if buildings[(nx, ny)] > 0:
                    buildings[(nx, ny)] -= 1
                    if buildings[(nx, ny)] == 0:
                        total -= 1
                        earthquake.append((nx, ny))
                else:
                    break
        else:
            break
# print(earthquake)
while earthquake:
    x, y = earthquake.pop(0)
    for dx, dy in dix:
        nx, ny = x + dx, y + dy
        if N > nx >= 0 and M > ny >= 0 and (nx, ny) not in walls:
            what = pan[nx][ny]
            if what in "*#":
                if buildings[(nx, ny)] > 0:
                    buildings[(nx, ny)] -= 1
                    if buildings[(nx, ny)] == 0:
                        total -= 1
                        earthquake.append((nx, ny))
print(total_answer-total, total)