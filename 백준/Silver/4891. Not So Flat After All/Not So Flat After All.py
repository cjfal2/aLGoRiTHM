import sys
input = sys.stdin.readline

def prime_factors(n):
    i = 2
    factors = {}
    while i * i <= n:
        while n % i == 0:
            if i in factors:
                factors[i] += 1
            else:
                factors[i] = 1
            n //= i
        i += 1
    if n > 1:
        factors[n] = 1
    return factors

case_num = 1
while True:
    line = input()
    if not line:
        break
    A, B = map(int, line.strip().split())
    if A == 0 and B == 0:
        break

    fa = prime_factors(A)
    fb = prime_factors(B)

    primes = set(fa.keys()) | set(fb.keys())  # 합집합
    distance = 0
    for p in primes:
        distance += abs(fa.get(p, 0) - fb.get(p, 0))

    print(f"{case_num}. {len(primes)}:{distance}")
    case_num += 1
