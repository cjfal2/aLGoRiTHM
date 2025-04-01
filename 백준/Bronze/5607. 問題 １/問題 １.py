import sys
input = sys.stdin.readline

n = int(input())
score_a = 0
score_b = 0

for _ in range(n):
    a, b = map(int, input().split())
    if a > b:
        score_a += a + b
    elif a < b:
        score_b += a + b
    else:
        score_a += a
        score_b += b

print(f"{score_a} {score_b}")
