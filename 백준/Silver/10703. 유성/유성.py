R, S = map(int, input().split())
grid = [list(input().strip()) for _ in range(R)]

meteor_bottom = [-1] * S
ground_top = [R] * S

for i in range(R):
    for j in range(S):
        if grid[i][j] == 'X':
            meteor_bottom[j] = max(meteor_bottom[j], i)
        elif grid[i][j] == '#':
            ground_top[j] = min(ground_top[j], i)

fall_distance = min(ground_top[j] - meteor_bottom[j] - 1 for j in range(S) if meteor_bottom[j] != -1)

for i in range(R - 1, -1, -1):
    for j in range(S):
        if grid[i][j] == 'X':
            grid[i][j] = '.'
            grid[i + fall_distance][j] = 'X'

print("\n".join("".join(row) for row in grid))
