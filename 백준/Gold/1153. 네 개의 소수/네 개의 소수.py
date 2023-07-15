def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**(0.5)) + 1):
        if not num % i:
            return False
    return True


def gold(number):
    '''
    ### 골드바흐의 추측 #

    2보다 큰 모든 짝수는 2개의 소수의 합으로 표현할 수 있다.
    홀수 2 + 3 + a + b
    또는
    짝수 2 + 2 + a + b
    -> 1,2,3,4,5,6,7 은 -1
    '''
    for x in range(len(primes)):
        for y in range(len(primes)):
            temp = primes[x] + primes[y]
            if temp == number:
                for q in [x, y]:
                    answer.append(primes[q])
                return
            elif temp > number:
                break


N = int(input())

primes = []
for i in range(2, N + 1):
    if is_prime(i):
        primes.append(i)


if N < 8:
    print(-1)
else:
    answer = [2]

    if N % 2: # 홀수
        answer.append(3)
        N -= 5
    else: # 짝수
        answer.append(2)
        N -= 4

    gold(N)
    print(*answer)
