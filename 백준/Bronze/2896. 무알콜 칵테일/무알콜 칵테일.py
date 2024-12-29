A, B, C = map(int, input().split())
I, J, K = map(int, input().split())

a = A / I
b = B / J
c = C / K
min_value = min(a, b, c)
print(A - min_value * I, B - min_value * J, C - min_value * K)

