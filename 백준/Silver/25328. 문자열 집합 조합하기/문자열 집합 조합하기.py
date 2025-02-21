import sys
from itertools import combinations
from collections import Counter

# 입력 받기
x = input().strip()
y = input().strip()
z = input().strip()
k = int(input().strip())

# 조합 생성 함수
def get_combinations(s, k):
    return {''.join(c) for c in combinations(s, k)}

# 각 문자열에 대한 조합 생성
comb_x = get_combinations(x, k)
comb_y = get_combinations(y, k)
comb_z = get_combinations(z, k)

# 조합들을 합쳐서 등장 횟수 세기
all_combs = list(comb_x) + list(comb_y) + list(comb_z)
counter = Counter(all_combs)

# 두 번 이상 등장한 조합 필터링 및 정렬
result = sorted([key for key, value in counter.items() if value >= 2])

# 결과 출력
print('\n'.join(result) if result else -1)
