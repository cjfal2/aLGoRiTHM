n=int(input())
visited_sero = [[0 for _ in range(n)] for _ in range(n)]
visited_garo = [[0 for _ in range(n)] for _ in range(n)]
directions = {
    "D": (1, 0),
    "U": (-1, 0),
    "R": (0, 1),
    "L": (0, -1),
}
x, y = 0, 0
command = input()
for c in command:
    dx, dy = directions[c]
    if n > x >= 0 and n > y >= 0 and n > x + dx >= 0 and n > y + dy >= 0:
        if c in "UD":
            visited_sero[x][y] = 1
        else:
            visited_garo[x][y] = 1
        x += dx
        y += dy
        if c in "UD":
            visited_sero[x][y] = 1
        else:
            visited_garo[x][y] = 1
    else:
        continue
pan = [["." for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited_sero[i][j] == 1 and visited_garo[i][j] == 1:
            pan[i][j] = "+"
        elif visited_garo[i][j] == 1:
            pan[i][j] = "-"
        elif visited_sero[i][j] == 1:
            pan[i][j] = "|"
    print(*pan[i], sep="")

