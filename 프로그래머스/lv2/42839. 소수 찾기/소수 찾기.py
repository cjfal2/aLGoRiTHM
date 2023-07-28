def eratosthenes(max_num):
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(max_num**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_num + 1, i):
                sieve[j] = False

    primes = [num for num, is_prime in enumerate(sieve) if is_prime]
    return primes


def solution(numbers):
    max_num = int('9' * len(numbers))  # 주어진 숫자로 만들 수 있는 가장 큰 수를 구함
    primes = set(eratosthenes(max_num))

    def permu(n, arr, v, c):
        if c and n not in check and int(n) in primes:
            check.add(int(n))
        if n != "":
            n = str(n)
            if len(n) == len(arr):
                return

        for i in range(len(arr)):
            if not v[i]:
                v[i] = 1
                permu(n + arr[i], arr, v, 1)
                v[i] = 0

    check = set()
    visited = [0] * len(numbers)
    permu("", numbers, visited, 0)

    return len(check)