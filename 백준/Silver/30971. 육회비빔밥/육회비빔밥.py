import itertools

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

max_taste = -1

# 모든 순열에 대해 계산
for perm in itertools.permutations(range(N)):
    total_taste = 0
    flag = True
    for i in range(1, N):
        if C[perm[i-1]] * C[perm[i]] > K:
            flag = False
            break
        total_taste += A[perm[i-1]] * B[perm[i]]

    if flag:
        max_taste = max(max_taste, total_taste)

print(max_taste)  # 결과 출력
