N = int(input())
pan = [list(input()) for _ in range(N)]
mines = set()
for n in range(N):
    for m in range(N):
        if pan[n][m] != ".":
            pan[n][m] = int(pan[n][m])
            mines.add((n, m))

def find_mine(i, j):
    temp = 0
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if N > x >= 0 and N > y >= 0:
                if (x, y) in mines:
                    temp += pan[x][y]
    return temp


for n in range(N):
    for m in range(N):
        if pan[n][m] == ".":
            num = find_mine(n, m)
            pan[n][m] = num if num <10 else "M"

for n, m in mines:
    pan[n][m] = "*"

for p in pan:
    print(*p, sep="")