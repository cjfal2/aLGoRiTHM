import math

for _ in range(int(input())):
    A, B, X = map(int, input().split())
    g = math.gcd(A, B)
    print(X // g)
