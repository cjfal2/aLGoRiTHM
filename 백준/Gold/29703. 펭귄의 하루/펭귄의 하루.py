N, M = map(int, input().split())
pan = []
flag = True
for i in range(N):
    maps = input()
    if flag:
        for j in range(M):
            if maps[j] == "S":
                si, sj = i, j
    pan.append(maps)


def bfs1(i, j):
    temp = []
    visited_fish = [[0 for _ in range(M)] for _ in range(N)]
    visited_fish[i][j] = 1

    visited_home = [[0 for _ in range(M)] for _ in range(N)]

    q = [(i, j, 0, "F")]
    while q:
        x, y, c, target = q.pop(0)
        for dx, dy in (1, 0), (-1, 0), (0, -1), (0, 1):
            nx, ny = x + dx, y + dy
            if N > nx >= 0 and M > ny >= 0 and pan[nx][ny] != "D":
                if target == "F" and not visited_fish[nx][ny]:
                    if pan[nx][ny] == "F":
                        q.append((nx, ny, c+1, "H"))
                        visited_home[nx][ny] = 1
                    else:
                        q.append((nx, ny, c+1, "F"))
                        visited_fish[nx][ny] = 1

                elif target == "H" and not visited_home[nx][ny]:
                    if pan[nx][ny] == "H":
                        temp.append(c+1)
                    else:
                        q.append((nx, ny, c+1, "H"))
                        visited_home[nx][ny] = 1

    return min(temp) if temp else -1


print(bfs1(si, sj))
