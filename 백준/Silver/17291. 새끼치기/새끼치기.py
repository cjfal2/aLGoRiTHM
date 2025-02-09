import sys

N = int(sys.stdin.readline())

# 각 벌레는 (태어난 해, 분열 횟수)를 저장
bugs = [(1, 0)]  # 1년 2월에 태어난 벌레 1마리

for year in range(2, N + 1):
    new_bugs = []
    for birth_year, division_count in bugs:
        # 분열
        new_bugs.append((birth_year, division_count + 1))  # 기존 벌레
        new_bugs.append((year, 0))  # 새로운 벌레

    # 사망 처리
    alive_bugs = []
    for birth_year, division_count in new_bugs:
        if birth_year % 2 == 1 and division_count >= 3:  # 홀수년도 태어난 벌레 사망
            continue
        if birth_year % 2 == 0 and division_count >= 4:  # 짝수년도 태어난 벌레 사망
            continue
        alive_bugs.append((birth_year, division_count))

    bugs = alive_bugs

print(len(bugs))