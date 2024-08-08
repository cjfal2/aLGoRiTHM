def is_prime():
    temp = []
    for num in range(2, 104730):
        for i in range(2, int(num**(0.5)) + 1):
            if not num % i:
                break
        else:
            temp.append(num)
    return temp

primes = is_prime()
print(primes[int(input())-1])