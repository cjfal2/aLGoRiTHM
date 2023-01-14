from itertools import permutations
from copy import deepcopy

N = int(input()) # 물약의 종류 N개
C = [0] + list(map(int, input().split())) # 물약의 가격
# 물약의 할인 정보 N개
P = [[] for _ in range(N+1)]
for i in range(1, N+1):
    A = []
    for _ in range(int(input())):
        A.append(list(map(int, input().split())))
    P[i] = A

ans = 9999999999
for comb in permutations(list(range(1, N+1)), N):
    total = 0
    boksa = deepcopy(C)
    for c in comb:
        total += boksa[c]
        for p in P[c]:
            boksa[p[0]] -= p[1]
            if boksa[p[0]] <= 0:
                boksa[p[0]] = 1
    ans = min(ans, total)
print(ans)
