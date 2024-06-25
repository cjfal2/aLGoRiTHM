from itertools import combinations


N, L, R, X = map(int, input().split())
# 문제수, 난이도의합 범위 L~R, 민맥스 차이 X
problems = sorted(map(int, input().split()))

answer = 0
for n in range(2, N+1):
    for combi in combinations(problems, n):
        s = sum(combi)
        if L > s or s > R:
            continue
        
        x = max(combi) - min(combi)
        if x < X:
            continue

        answer += 1

print(answer)