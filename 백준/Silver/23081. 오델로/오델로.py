# 8방향 체크
def flip_white(i, j, board):
    global max_flips, answer
    total_flip_white = 0
    for dx, dy in dix:
        nx, ny = i, j
        white_num = 0
        while 1:
            # print(i,j, [dx, dy], nx, ny)
            nx += dx
            ny += dy
            if N > nx >= 0 and N > ny >= 0:
                if board[nx][ny] == "W":
                    white_num += 1
                elif board[nx][ny] == ".":
                    break
                else:
                    total_flip_white += white_num
                    break
            else:
                break


    if max_flips < total_flip_white:
        max_flips = total_flip_white
        answer = i, j


dix = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
N = int(input())
pan = [list(input()) for _ in range(N)]

max_flips = 0
answer = [-1, -1]

for n in range(N):  # 세로
    for m in range(N):  # 가로
        if pan[n][m] == ".":
            flip_white(n, m, pan)
if answer == [-1, -1]:
    print("PASS")
else:    
    print(*answer[::-1])
    print(max_flips)
