MAX_SIZE = 19
matrix = []
count = []

# 오른쪽, 오른쪽 대각선, 아래, 왼쪽 대각선 탐색
dx = [1, 1, 0, -1]
dy = [0, 1, 1, 1]

def update_count(x, y, dir):
    nx = x + dx[dir]
    ny = y + dy[dir]

    if matrix[nx][ny] == matrix[x][y]:
        count[nx][ny][dir] = update_count(nx, ny, dir) + 1
        return count[nx][ny][dir]
    return 1

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    global matrix, count
    matrix = [[0] * (MAX_SIZE + 2) for _ in range(MAX_SIZE + 2)]
    count = [[[0] * 4 for _ in range(MAX_SIZE + 2)] for _ in range(MAX_SIZE + 2)]

    index = 0
    for i in range(1, MAX_SIZE + 1):
        for j in range(1, MAX_SIZE + 1):
            matrix[i][j] = int(data[index])
            index += 1

    for j in range(1, MAX_SIZE + 1):
        for i in range(1, MAX_SIZE + 1):
            if matrix[i][j] != 0:
                for dir in range(4):
                    if count[i][j][dir] == 0 and update_count(i, j, dir) == 5:
                        print(matrix[i][j])
                        print(i, j)
                        return

    print(0)

if __name__ == "__main__":
    main()
