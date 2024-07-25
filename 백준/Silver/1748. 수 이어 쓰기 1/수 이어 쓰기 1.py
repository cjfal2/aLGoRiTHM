def solve(n):
    total = 0
    length = 1
    temp = 10

    while n >= temp:
        total += (temp - temp // 10) * length
        length += 1
        temp *= 10

    total += (n - temp // 10 + 1) * length
    return total


print(solve(int(input())))
