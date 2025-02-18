import sys
input = sys.stdin.readline

X, Y, W, S = map(int, input().split())

# Case 1: 모두 직선 이동
case1 = (X + Y) * W

# Case 2: 대각선 최대한 이동 + 나머지 직선 이동
case2 = min(X, Y) * S + abs(X - Y) * W

# Case 3: 대각선만 이동 (짝수와 홀수 처리)
# (X + Y) 가 짝수면 모두 대각선 이동 가능
if (X + Y) % 2 == 0:
    case3 = max(X, Y) * S
# 홀수면 마지막 1칸 직선 이동 필요
else:
    case3 = (max(X, Y) - 1) * S + W

print(min(case1, case2, case3))
