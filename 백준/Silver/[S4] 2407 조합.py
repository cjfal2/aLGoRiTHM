from fractions import Fraction

n, m = map(int, input().split())
A = list(range(n, n-m, -1))
B = list(range(m, 0, -1))

a = 1
for a1 in A:
    a *= a1
b = 1
for b1 in B:
    b *= b1
print(Fraction(a, b))
