def solution(n):
    answer = 0
    sieve = [True] * (n+1)
    p = 2
    while p**2 <= n:
        if sieve[p] == True:
            for i in range(p**2, n+1, p):
                sieve[i] = False
        p += 1
    for p in range(2, n+1):
        if sieve[p]:
            answer+=1

    return answer