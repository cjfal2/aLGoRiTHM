import sys
input = sys.stdin.readline
a, b, n = map(int, input().split())
a %= b # 처음에 a를 b로 나눔
# 나눗셈 구현 n-1 까지
for _ in range(n - 1):
    a = (a * 10) % b
# 나눗셈의 몫 출력 n 번째는
print((a * 10) // b )