import math


def solve(a, b, c, d):
    n = a * c
    q = b * d * 2

    g = math.gcd(n, q)
    n //= g
    q //= g

    return 1 if q == 1 else 0


while 1:
    try:
        a, b, c, d = map(int, input().split())
        print(solve(a, b, c, d))
    except:
        break
