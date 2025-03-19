import sys
input = sys.stdin.readline

N = int(input().strip())
cows = []

for _ in range(N):
    sign, p = input().strip().split()
    p = int(p)
    cows.append((sign, p))

# 가능한 모든 p 값 정렬
possible_positions = sorted(set(p for _, p in cows))

min_lies = N  # 거짓말 최소값 초기화

for pos in possible_positions:
    lies = 0
    for sign, p in cows:
        if sign == 'G' and pos < p:
            lies += 1
        elif sign == 'L' and pos > p:
            lies += 1
    min_lies = min(min_lies, lies)

print(min_lies)
