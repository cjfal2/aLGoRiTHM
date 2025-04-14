# 방향 명령어를 (dx, dy)로 매핑
dir_map = {
    'R':  (1, 0),
    'L':  (-1, 0),
    'B':  (0, -1),
    'T':  (0, 1),
    'RT': (1, 1),
    'LT': (-1, 1),
    'RB': (1, -1),
    'LB': (-1, -1),
}

# 체스 좌표를 (x, y)로 변환
def to_pos(s):
    col = ord(s[0]) - ord('A')  # A~H → 0~7
    row = int(s[1]) - 1         # 1~8 → 0~7
    return (col, row)

# (x, y)를 체스 좌표로 변환
def to_str(pos):
    x, y = pos
    return chr(x + ord('A')) + str(y + 1)

# 입력
king_str, stone_str, n = input().split()
n = int(n)
commands = [input().strip() for _ in range(n)]

king = to_pos(king_str)
stone = to_pos(stone_str)

for cmd in commands:
    dx, dy = dir_map[cmd]
    nx, ny = king[0] + dx, king[1] + dy

    # 킹이 체스판 안인지 확인
    if not (0 <= nx < 8 and 0 <= ny < 8):
        continue

    # 돌이랑 위치 겹치는 경우
    if (nx, ny) == stone:
        sx, sy = stone[0] + dx, stone[1] + dy
        if not (0 <= sx < 8 and 0 <= sy < 8):
            continue  # 돌이 못 움직이면 둘 다 못 감
        stone = (sx, sy)

    king = (nx, ny)

# 출력
print(to_str(king))
print(to_str(stone))
