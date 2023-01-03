import sys
input = sys.stdin.readline

def memory(direction):
    global sero_max, sero_min, garo_max, garo_min
    if direction in [1, 3]:
        sero_max = max(sero_max, y)
        sero_min = min(sero_min, y)
    else:
        garo_max = max(garo_max, x)
        garo_min = min(garo_min, x)

dix = [[-1, 0], [0, -1], [1, 0], [0, 1]]
for _ in range(int(input().strip())):
    d = 1 # 1 북 , 0 서, 2 동, 3 남
    x = y = sero_max = sero_min = garo_max = garo_min = 500
    for command in input().strip():
        if command == 'F':
            x += dix[d][0]
            y += dix[d][1]
            memory(d)

        elif command == 'B':
            x -= dix[d][0]
            y -= dix[d][1]
            memory(d)

        elif command == 'L':
            d -= 1
            if d < 0:
                d = 3
        elif command == 'R':
            d += 1
            if d > 3:
                d = 0
                
    print((sero_max-sero_min) * (garo_max-garo_min))
