def solve(trophies):
    left = 1
    right = 1

    left_max = trophies[0]
    for trophy in trophies[1:]:
        if trophy > left_max:
            left += 1
            left_max = trophy

    right_max = trophies[-1]
    for trophy in reversed(trophies[:-1]):
        if trophy > right_max:
            right += 1
            right_max = trophy

    return left, right

# 트로피 개수 입력
N = int(input())

# 트로피 높이 입력
trophies = [int(input()) for _ in range(N)]

# 보이는 트로피 개수 계산
left_count, right_count = solve(trophies)

# 결과 출력
print(left_count)
print(right_count)