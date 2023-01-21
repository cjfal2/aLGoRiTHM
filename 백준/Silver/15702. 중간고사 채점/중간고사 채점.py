import sys
input = sys.stdin.readline

# N: 문제의 수, M: 응시자 수
N, M = map(int, input().strip().split())
# 각 문제의 배점
scores = list(map(int, input().strip().split()))

info = dict()
for _ in range(M):
    num_student, *get_score = input().strip().split()
    num_student = int(num_student)
    total_score = 0
    for idx, OX in enumerate(get_score):
        if OX == 'O':
            total_score += scores[idx]
    info[num_student] = total_score
print(*sorted(list(filter(lambda g: g[1] == max(info.values()), list(info.items()))))[0])
