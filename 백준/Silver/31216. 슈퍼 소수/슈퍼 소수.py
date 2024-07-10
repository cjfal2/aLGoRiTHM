def is_prime(number):
    '''
    에라토스테네스의 체
    number의 최대 약수가 sqrt(number) 이하이므로 i=sqrt(number)까지 검사
    '''
    if number < 2:
        return False

    for m in range(2, int(number ** 0.5) + 1):
        if not number % m:
            return False  # 소수가 아니다.
    return True  # 소수가 맞다.


def find_super_primes(n):
    '''
    n번째 슈퍼 소수를 찾는 함수
    '''
    primes = []
    super_primes = []
    num = 2
    while len(super_primes) < n:
        if is_prime(num):
            primes.append(num)
            if is_prime(len(primes)):
                super_primes.append(num)
        num += 1
    return super_primes


super_primes = find_super_primes(3001)
for _ in range(int(input())):
    print(super_primes[int(input()) - 1])