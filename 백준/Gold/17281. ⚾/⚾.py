import sys
input = sys.stdin.readline
from itertools import permutations

def game(order):
    order.insert(3, 0)
    out = 0 # 아웃 카운트
    innings = 0 # 이닝 수
    bat_point = 0 # 타석
    base1, base2, base3, score = 0, 0, 0, 0 # 1루 2루 3루 점수
    while 1:
        batting = players[innings][order[bat_point]]
        if not batting:
            out += 1
            bat_point = (bat_point + 1) % 9
            if out == 3:
                out = 0
                innings += 1
                base1, base2, base3 = 0, 0, 0
                if innings == N:
                    return score

        elif batting == 1:
            bat_point = (bat_point + 1) % 9
            if base3:
                base3 = 0
                score += 1
            if base2:
                base2 = 0
                base3 = 1
            if base1:
                base1 = 0
                base2 = 1
            if not base1:
                base1 = 1

        elif batting == 2:
            bat_point = (bat_point + 1) % 9
            if base3:
                base3 = 0
                score += 1
            if base2:
                base2 = 0
                score += 1
            if base1:
                base1 = 0
                base3 = 1
            if not base2:
                base2 = 1

        elif batting == 3:
            bat_point = (bat_point + 1) % 9
            if base3:
                base3 = 0
                score += 1
            if base2:
                base2 = 0
                score += 1
            if base1:
                base1 = 0
                score += 1
            if not base3:
                base3 = 1

        elif batting == 4:
            bat_point = (bat_point + 1) % 9
            if base3:
                base3 = 0
                score += 1
            if base2:
                base2 = 0
                score += 1
            if base1:
                base1 = 0
                score += 1
            score += 1
            


N = int(input().strip())
players = [list(map(int, input().strip().split())) for _ in range(N)] # 선수들을 리스트로 생성

max_score = 0
for perm in permutations(list(range(1, 9)), 8):
    game_score = game(list(perm))
    max_score = max(max_score, game_score)

print(max_score)