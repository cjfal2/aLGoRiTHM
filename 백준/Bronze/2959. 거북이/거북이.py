from itertools import permutations

def solve(A, B, C, D):
    max_area = 0
    for perm in permutations([A, B, C, D]):  # 가능한 모든 순열을 고려
        width = min(perm[0], perm[2])  # 가로 길이 계산
        height = min(perm[1], perm[3])  # 세로 길이 계산
        area = width * height
        max_area = max(max_area, area)  # 최대 면적 갱신
    return max_area

A, B, C, D = map(int, input().split())

max_area = solve(A, B, C, D)
print(max_area)
