def is_valid_grid(n, grid):
    for i in range(n):
        row = grid[i]
        col = [grid[j][i] for j in range(n)]
        
        if row.count('B') != n // 2 or row.count('W') != n // 2:
            return 0
        if col.count('B') != n // 2 or col.count('W') != n // 2:
            return 0

    for i in range(n):
        for j in range(n - 2):
            if grid[i][j] == grid[i][j+1] == grid[i][j+2]:
                return 0
            if grid[j][i] == grid[j+1][i] == grid[j+2][i]:
                return 0

    return 1

if __name__ == "__main__":
    n = int(input())
    grid = [input().strip() for _ in range(n)]
    print(is_valid_grid(n, grid))
