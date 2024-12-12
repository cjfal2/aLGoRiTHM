import math

for _ in range(int(input())):
    numbers = list(map(int, input().split()))
    max_gcd = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            gcd = math.gcd(numbers[i], numbers[j])
            max_gcd = max(max_gcd, gcd)
    print(max_gcd)