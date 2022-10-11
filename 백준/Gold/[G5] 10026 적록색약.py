def RGBFS1(color, i, j):
    q = [(i, j)]
    pan1[i][j] = 0  # 찾았으니 처음거를 0으로 바꿔줌
    while q:     # bfs
        x, y = q.pop(0)
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx, ny = x + dx, y + dy
            if N > nx >= 0 and N > ny >= 0 and pan1[nx][ny] == color:
                pan1[nx][ny] = 0       # 0으로 덮어버려서 다시는 못찾게 함
                q.append((nx, ny))  # bfs 돌 수 있게함


def RGBFS2(color, i, j):
    q = [(i, j)]
    pan2[i][j] = 0  # 찾았으니 처음거를 0으로 바꿔줌
    while q:     # bfs
        x, y = q.pop(0)
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx, ny = x + dx, y + dy
            if N > nx >= 0 and N > ny >= 0 and pan2[nx][ny] == color:
                pan2[nx][ny] = 0       # 0으로 덮어버려서 다시는 못찾게 함
                q.append((nx, ny))  # bfs 돌 수 있게함


N = int(input())
pan1 = []
pan2 = []
for i in range(N):
    inp = list(input())
    pan1.append(inp)
    temp = []
    for j in range(N):
        if inp[j] == 'G':
            temp.append('R')
        else:
            temp.append(inp[j])
    pan2.append(temp)

RGB1 = 0
RGB2 = 0
for s in range(N):
    for g in range(N):
        if pan1[s][g]:
            RGB1 += 1
            RGBFS1(pan1[s][g], s, g)
        if pan2[s][g]:
            RGB2 += 1
            RGBFS2(pan2[s][g], s, g)

print(RGB1, RGB2)
