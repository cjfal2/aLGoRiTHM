pan = [input() for _ in range(8)]
co = 0
for i in range(0,8,2):
    for j in range(0,8,2):
        if pan[i][j] == 'F':
            co += 1
for x in range(1,8,2):
    for y in range(1,8,2):
        if pan[x][y] == 'F':
            co += 1
print(co)