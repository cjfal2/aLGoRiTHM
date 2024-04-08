# https://www.acmicpc.net/problem/23288
"""
1. 이동하기 => 주사위의 면, 방향, 구르면 어디면인지, 벽이라면 반대로 방향 바뀜

2. 점수 구하기 => bfs

3. 이동 방향 결정 (회전은 없음)
주사위 > 판 => 90 시계
주사위 < 판 => 90 반시계
주사위 = 판 => 그대로
"""

N, M, K = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(N)]
dice = {
    "U": 1,
    "D": 6,
    "L": 4,
    "R": 3,
    "F": 5,
    "B": 2
}
dix = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북 동 남 서
now_direction = 1
now_x, now_y = 0, 0
answer = 0


def roll_dice(direction):
    if direction == 1:
        dice["U"], dice["D"], dice["L"], dice["R"] = dice["L"], dice["R"], dice["D"], dice["U"]
    elif direction == 3:
        dice["U"], dice["D"], dice["L"], dice["R"] = dice["R"], dice["L"], dice["U"], dice["D"]
    elif direction == 0:
        dice["U"], dice["D"], dice["F"], dice["B"] = dice["F"], dice["B"], dice["D"], dice["U"]
    else:
        dice["U"], dice["D"], dice["F"], dice["B"] = dice["B"], dice["F"], dice["U"], dice["D"]
    return


def get_score(wx, wy):
    what_number = pan[wx][wy]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[wx][wy] = 1
    q = [(wx, wy)]
    score = 1
    while q:
        x, y = q.pop(0)
        for dx, dy in (1, 0), (-1, 0), (0, -1), (0, 1):
            nx, ny = x + dx, y + dy
            if N > nx >= 0 and M > ny >= 0 and not visited[nx][ny] and pan[nx][ny] == what_number:
                q.append((nx, ny))
                visited[nx][ny] = 1
                score += 1
    return score * what_number


def change_direction(i, j):
    global now_direction

    pan_number = pan[i][j]
    dice_number = dice["D"]
    if pan_number < dice_number:
        now_direction = (now_direction + 1) % 4
    elif pan_number > dice_number:
        now_direction = (now_direction - 1) % 4


for _ in range(K):
    while True:
        ix = now_x + dix[now_direction][0]
        iy = now_y + dix[now_direction][1]
        if N > ix >= 0 and M > iy >= 0:  # 판 안쪽에 위치할 경우
            # 주사위 굴리기
            roll_dice(now_direction)
            answer += get_score(ix, iy)
            change_direction(ix, iy)
            now_x, now_y = ix, iy
            break
        else:
            now_direction = (now_direction + 2) % 4

print(answer)
