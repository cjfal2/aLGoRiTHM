def find_cookie_body(n, grid):
    # 심장 위치 찾기
    heart_x, heart_y = 0, 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '*' and grid[i - 1][j] == '*':
                heart_x, heart_y = i + 1, j + 1  # 1-indexed
                break
        if heart_x != 0:
            break

    # 왼쪽 팔 길이 계산
    left_arm_length = 0
    for j in range(heart_y - 2, -1, -1):
        if grid[heart_x - 1][j] == '*':
            left_arm_length += 1
        else:
            break

    # 오른쪽 팔 길이 계산
    right_arm_length = 0
    for j in range(heart_y, n):
        if grid[heart_x - 1][j] == '*':
            right_arm_length += 1
        else:
            break

    # 허리 길이 계산
    waist_length = 0
    for i in range(heart_x, n):
        if grid[i][heart_y - 1] == '*':
            waist_length += 1
        else:
            break

    # 왼쪽 다리 길이 계산
    left_leg_length = 0
    for i in range(heart_x + waist_length, n):
        if grid[i][heart_y - 2] == '*':
            left_leg_length += 1
        else:
            break

    # 오른쪽 다리 길이 계산
    right_leg_length = 0
    for i in range(heart_x + waist_length, n):
        if grid[i][heart_y] == '*':
            right_leg_length += 1
        else:
            break

    print(heart_x, heart_y)
    print(left_arm_length, right_arm_length, waist_length, left_leg_length, right_leg_length)


n = int(input())
grid = [input().strip() for _ in range(n)]
find_cookie_body(n, grid)
