import math

def solve(n):
    if n == 1:
        return 0
    
    count = n - 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            count -= count // i
            while n % i == 0:
                n //= i
    if n > 1:
        count -= count // n
    return count

while 1:
    n = int(input())
    if n == 0:
        break
    print(solve(n))
