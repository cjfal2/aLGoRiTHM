dix = {
    '0': ( 0,  1), # 0: x좌표가 증가하는 방향 (→)
    '1': (-1,  0), # 1: y좌표가 감소하는 방향 (↑)
    '2': ( 0, -1), # 2: x좌표가 감소하는 방향 (←)
    '3': ( 1,  0), # 3: y좌표가 증가하는 방향 (↓)
}

generation = {
    0: ['0'],
    1: ['1'],
    2: ['2'],
    3: ['3'],
}


N = int(input())
max_g = 0
L = []
for _ in range(N):
    x, y, d, g = map(int, input().split())
    L.append((y, x, d, g))
    max_g = max(max_g, g)

# generation 채우는 식 => 인풋 세대의 max값
for gen in range(max_g):
    for di in range(4):
        ne = di + 1
        if ne == 4:
            ne = 0
        generation[di].append(generation.get(di)[gen] + generation.get(ne)[gen][::-1])

pan = [[0 for _ in range(102)] for _ in range(102)]
# pan = [[0 for _ in range(20)] for _ in range(20)]

ones = set()
for x, y, d, g in L:
    gogo = generation.get(d)[g]
    pan[x][y] = 1
    ones.add((x, y))
    for num in gogo:
        nx, ny = dix.get(num)
        x += nx
        y += ny
        pan[x][y] = 1
        ones.add((x, y))


'''
우,하,우하 좌표에 1이 있는지 확인한다.
100x100 101x101은 인덱스에러가 난다.
'''
ans = 0
for x, y in ones:
    if pan[x+1][y] == pan[x][y+1] == pan[x+1][y+1] == 1:
        ans += 1
print(ans)