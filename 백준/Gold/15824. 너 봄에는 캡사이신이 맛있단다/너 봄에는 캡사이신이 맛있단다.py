import sys
input = sys.stdin.readline
mod = 10**9 + 7

n = int(input())
a = list(map(int, input().split()))
a.sort()

# 2의 제곱 미리 계산
p = [1] * n
for i in range(1, n):
    p[i] = p[i-1] * 2 % mod

# max−min 차이 합 계산
res = 0
for i, v in enumerate(a):
    res = (res + v * (p[i] - p[n-1-i])) % mod

print(res)
