def sel_island():
    global co, memory
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and pan[i][j]:
                visited[i][j] = 1
                co += 1
                pan[i][j] = co
                q = [(i, j)]
                p = []
                while q:
                    x, y = q.pop(0)
                    for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                        nx, ny = x + dx, y + dy
                        if N > nx >= 0 and N > ny >= 0:
                            if not visited[nx][ny]:
                                if pan[nx][ny]:
                                    q.append((nx, ny))
                                    visited[nx][ny] = 1
                                    pan[nx][ny] = co
                                else:
                                    if (x, y) not in p:
                                        p.append((x, y))

                memory.append(p)

def make_bridge(where):
    global MIN, memory
    for xx, yy in memory[where]:
        visited = [[0 for _ in range(N)] for _ in range(N)]
        visited[xx][yy] = 1
        q = [(xx, yy)]
        flag = True
        while q and flag:
            x, y = q.pop(0)
            for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                nx, ny = x + dx, y + dy
                if N > nx >= 0 and N > ny >= 0:
                    if not visited[nx][ny]:
                        if not pan[nx][ny]:
                            q.append((nx, ny))
                            visited[nx][ny] = visited[x][y] + 1
                        elif pan[nx][ny] != 0 and pan[nx][ny] != where:
                            MIN = min(visited[x][y]-1, MIN)
                            flag = False
                            break


N = int(input())
pan = [list(map(int, input().split())) for _ in range(N)]
co = 1
memory = [[], []]
sel_island()
# for v in pan:
#     print(v)
# # print(co)  -> 2, 3, 4
# for m in memory:
#     print(m)
MIN = 9999999999999999999
for i in range(2, co+1):
    make_bridge(i)
print(MIN)