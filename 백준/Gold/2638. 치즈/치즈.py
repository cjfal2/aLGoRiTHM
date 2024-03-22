N, M = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(N)]
cheeze_num = 0
for i in range(N):
    for j in range(M):
        if pan[i][j]:
            cheeze_num += 1
direc = ((1, 0), (-1, 0), (0, -1), (0, 1))


def find_air():
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[0][0] = 1
    q = [(0, 0)]
    while q:
        x, y = q.pop(0)
        for dx, dy in direc:
            nx, ny = x + dx, y + dy
            if N > nx >= 0 and M > ny >= 0 and not visited[nx][ny] and not pan[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny))
    return visited


answer = 0
while cheeze_num:
    air_zone = find_air()
    for i in range(N):
        for j in range(M):
            if pan[i][j]:
                flag = 0
                temp = []
                for di, dj in direc:
                    if flag > 1:
                        break
                    ni, nj = i + di, j + dj
                    if N > ni >= 0 and M > nj >= 0 and air_zone[ni][nj]:
                        flag += 1
                if flag > 1:
                    cheeze_num -= 1
                    pan[i][j] = 0
    answer += 1

print(answer)
