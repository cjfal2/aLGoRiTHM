from itertools import combinations

def min_skill_difference(N, skills):
    total_sum = sum(skills)
    half_N = N // 2
    min_diff = float('inf')

    # N명 중에서 N/2명을 뽑는 모든 조합을 구함
    for team_A in combinations(skills, half_N):
        team_A_sum = sum(team_A)
        team_B_sum = total_sum - team_A_sum
        min_diff = min(min_diff, abs(team_A_sum - team_B_sum))

    return min_diff

# 입력 처리
T = int(input().strip())

for i in range(1, T + 1):
    values = list(map(int, input().strip().split()))
    N = values[0]
    skills = values[1:]
    result = min_skill_difference(N, skills)
    print(f"Case #{i}: {result}")
