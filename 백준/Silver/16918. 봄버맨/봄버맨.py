import sys
input = sys.stdin.readline

def simulate_bomberman(R, C, N, grid):
    if N == 1:
        return grid
    
    def explode(grid):
        new_grid = [['O'] * C for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 'O':
                    new_grid[i][j] = '.'
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < R and 0 <= nj < C:
                            new_grid[ni][nj] = '.'
        return new_grid
    
    full_bomb_grid = [['O'] * C for _ in range(R)]
    first_explosion = explode(grid)
    second_explosion = explode(first_explosion)
    
    if N % 2 == 0:
        return full_bomb_grid
    elif (N // 2) % 2 == 1:
        return first_explosion
    else:
        return second_explosion

R, C, N = map(int, input().split())
grid = [list(input().strip()) for _ in range(R)]
result = simulate_bomberman(R, C, N, grid)

for row in result:
    print("".join(row))
