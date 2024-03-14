N = int(input())
pan = [list(map(lambda x: int(x) if x != "#" else x, list(input()))) for _ in range(N)]
dix = ((1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1))
answer = 0 if N <= 4 else (N-4) ** 2
for x in range(1, N-1):
    for y in range(1, N-1):
        if x in (1, N-2) or y in (1, N-2):
            for dx, dy in dix:
                if pan[x + dx][y + dy] == 0:
                    break
            else:
                for dx, dy in dix:
                    nx, ny = x + dx, y + dy
                    if pan[nx][ny] != "#":
                        pan[nx][ny] -= 1
                answer += 1
print(answer)
